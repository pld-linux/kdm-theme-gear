
%define		_theme		gear

Summary:	Gear KDM theme
Summary(pl):	Motyw KDM Gear
Name:		kdm-theme-%{_theme}
Version:	01
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/25454-%{_theme}.tar.gz
# Source0-md5:	45a43d6c8eb76545445a0f611bcf3951
URL:		http://www.kde-look.org/content/show.php?content=25454
Requires:	kdebase-desktop >= 9:3.2.0
Requires:	kdmtheme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gear KDM Theme.

%description -l pl
Motyw KDM Gear.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

install %{_theme}/*.{desktop,jpg,png,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/%{_theme}
