# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-logos
Version:        3
Release:        alt1_5
Summary:        Boot splash imagery for Sugar on a Stick

Group:          System/Base
License:        GPLv2+
URL:            http://git.sugarlabs.org/projects/sugar-logos
Source0:        http://download.sugarlabs.org/sources/external/sugar-logos/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  plymouth-theme-charge
Requires:       plymouth
Requires:       plymouth-plugin-two-step
Source44: import.info

%description
A boot splash screen for Sugar using Plymouth.


%prep
%setup -q


%build


%install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar/
for i in src/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar/
done

cp %{_datadir}/plymouth/themes/charge/{box,bullet,entry,lock}.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/sugar

%post
export LIB=%{_lib}
if [ $1 -eq 1 ]; then
    %{_sbindir}/plymouth-set-default-theme sugar
else
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "solar" ]; then
        %{_sbindir}/plymouth-set-default-theme sugar
    fi
fi


%postun
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "sugar" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi


%files
%doc COPYING AUTHORS
%{_datadir}/plymouth/themes/sugar/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 3-alt1_5
- new version; import from fc17 updates

