Name:           color-filesystem
Version:        1
Release:        alt2
Summary:        Color filesystem layout

Group:          System/Base
License:        Public Domain
BuildArch:      noarch

Requires:  filesystem

%description
This package provides some directories that are required/used to store color. 


%package -n rpm-macros-color
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description -n rpm-macros-color
Set of RPM macros for directories that are required/used to store color.

Install this package if you want to create RPM packages that use %name.

%prep
# Nothing to prep

%build
# Nothing to build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/icc
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/cmms
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/settings
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/color/icc

# rpm macros
mkdir -p $RPM_BUILD_ROOT%{_rpmmacrosdir}/
cat >$RPM_BUILD_ROOT%{_rpmmacrosdir}/color<<EOF
%%_colordir %%_datadir/color
%%_syscolordir %%_colordir
%%_icccolordir %%_colordir/icc
%%_cmmscolordir %%_colordir/cmms
%%_settingscolordir %%_colordir/settings
EOF

%files
%dir %{_datadir}/color
%dir %{_datadir}/color/icc
%dir %{_datadir}/color/cmms
%dir %{_datadir}/color/settings
%dir %{_var}/lib/color
%dir %{_var}/lib/color/icc

%files -n rpm-macros-color
%_rpmmacrosdir/color

%changelog
* Sat Jun 09 2012 Igor Vlasenko <viy@altlinux.ru> 1-alt2
- renamed macros.color -> color (around altbug 27426)

* Fri Jun 08 2012 Igor Vlasenko <viy@altlinux.ru> 1-alt1
- release for ALT Linux

