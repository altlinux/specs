%define teaname dnotebook

%define Name DNoteBook
Name: tcl-%teaname
Version: 0.1
Release: alt1
Summary: TkTable analogue for Ck
License: BSD
Group: Development/Tcl
URL: http://doro.poltava.ua
Source: %url/sysprg/%teaname-%version.tar.gz
Patch: %name-0.1-pkg.patch.gz
BuildArch: noarch

BuildRequires: tcl rpm-build-tcl

%description
Truncated TkTable analogue for Ck.


%prep
%setup -q -n %teaname
%patch -p1


%build
echo "auto_mkindex . %teaname.tcl" | tclsh


%install
install -pD -m 0755 demo %buildroot%_tcldatadir/%Name/demos/demo.tcl
install -m 0644 %teaname.tcl tclIndex %buildroot%_tcldatadir/%Name/
cat > %buildroot%_tcldatadir/%Name/pkgIndex.tcl <<__INDEX__
package ifneeded %Name %version [list source [file join \$dir %teaname.tcl]]
__INDEX__


%files
%doc Readme
%dir %_tcldatadir/%Name
%dir %_tcldatadir/%Name/demos
%_tcldatadir/%Name/*.tcl
%_tcldatadir/%Name/tclIndex
%_tcldatadir/%Name/demos/*


%changelog
* Fri Oct 05 2007 Led <led@altlinux.ru> 0.1-alt1
- fixed BuildRequires

* Tue Nov 28 2006 Led <led@altlinux.ru> 0.1-alt0.1
- initial build
