Name: kde4-style-iaora 
Summary: IaOra Theme for KDE4
Version: 0.2.5
Release: %mkrel 2
Source0: ia_ora-kde4-%{version}.tar.bz2
Patch0: kde4-style-iaora-nodebug.patch
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/theme/ia_ora-kde4/
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL 
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace-devel
Requires: kde4-style-iaora-common
Obsoletes: ia_ora-kde-kwin < 1.0.8-14
Obsoletes: ia_ora-kde < 1.0.8-14

%description
IaOra theme for KDE 4

%files 
%{_kde_plugindir}/styles/*
%{_kde_libdir}/kde4/kwin3_iaora.so
%{_kde_appsdir}/kwin/iaora.desktop

#--------------------------------------------------------------------------------

%package -n qt4-style-iaora
Summary: IaOra Theme for Qt4
Group: Graphical desktop/KDE
Requires: kde4-style-iaora-common

%description -n qt4-style-iaora
IaOra theme for Qt4

%files -n qt4-style-iaora
%{qt4plugins}/styles/libiaora-qt.so

#--------------------------------------------------------------------------------

%package common
Summary: Common files for IaOra in KDE4 and Qt4
Group: Graphical desktop/KDE

%description common
Common files for IaOra in KDE4 and Qt4

%files common
%{_kde_appsdir}/color-schemes/
%{_kde_appsdir}/kstyle/themes/
# remove the config for now
%exclude %{_kde_libdir}/kde4/kwin*config.so

#--------------------------------------------------------------------------------

%prep 
%setup -q -n ia_ora-kde4
%patch0 -p1 -b .nodebug

%build 
%cmake_kde4 
%make

%install
rm -rf $RPM_BUILD_ROOT
pushd build
%makeinstall_std
popd


%clean 
rm -rf $RPM_BUILD_ROOT 

