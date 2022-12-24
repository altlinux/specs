# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define build_docs 1

%define major   0
%define libname libmirisdr%{major}
%define devname libmirisdr-devel

Name:           libmirisdr
Version:        0.0.20130608
Release:        alt1_9
Summary:        Support programs for MRi2500
License:        GPLv2
Group:          Communications
URL:            http://cgit.osmocom.org/libmirisdr/
##TODO Try a more recent fork e.g. https://github.com/ericek111/libmirisdr-5
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ccmake cmake ctest
BuildRequires:  pkgconfig(libusb)

%if %{build_docs}
BuildRequires:  doxygen
BuildRequires:  texlive-texmf
BuildRequires:  graphviz
%endif
Source44: import.info
ExcludeArch: ppc64le

%description
Programs to control the Mirics MRi2500 based DVB dongle in raw mode, so
it can be used as a SDR receiver.

%package -n %{libname}
Summary:        SDR driver for MRi2500
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}

%description -n %{libname}
Library to run Mirics MRi2500 based DVB dongle as a SDR receiver.

%package -n %{devname}
Summary:        Development files for mirisdr
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
Library headers and other development files for mirisdr driver.

%package devel-doc
Summary:        Documentation for libmirisdr
Group:          Documentation
BuildArch:      noarch

%description devel-doc
Documentation for libmirisdr driver. HTML and PDF formats.

%prep
%setup -q -n %{name}

# remove buildtime from documentation
sed -i 's|^HTML_TIMESTAMP         = YES|HTML_TIMESTAMP         = NO|' Doxyfile.in

# fix version in .pc
sed -i -e 's,\(^Version:\).*,\1 %{version},' libmirisdr.pc.in

# fix libdir in .pc
sed -i -e 's,\(^set(libdir \\${exec_prefix}/lib\),\1${LIB_SUFFIX},' CMakeLists.txt

%build
%{mageia_cmake}
%mageia_cmake_build

#create documentation
%if %{build_docs}
cp Doxyfile.in Doxyfile
sed -i "s\@VERSION@\%{version}\1" Doxyfile
doxygen
cd doc/latex
  make refman.dvi
  dvips -o refman.ps refman.dvi
  ps2pdf refman.ps refman.pdf
cd -
%endif

%install
%mageia_cmake_install

rm %{buildroot}%{_libdir}/libmirisdr.a

%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib/pkgconfig %{buildroot}%{_libdir}
%endif

#install udev rules
install -Dpm644 mirisdr.rules %{buildroot}%{_udevrulesdir}/10-mirisdr.rules

#install documentation
%if %{build_docs}
mkdir -p %{buildroot}%{_docdir}/%{name}/pdf
cp -r doc/html %{buildroot}%{_docdir}/%{name}
cp -r doc/latex/*.pdf %{buildroot}%{_docdir}/%{name}/pdf
%endif

%files
%doc AUTHORS README
%{_bindir}/miri_*
%{_udevrulesdir}/10-mirisdr.rules
%if %{build_docs}
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/pdf
%endif

%files -n %{libname}
%{_libdir}/libmirisdr.so.%{major}*

%files -n %{devname}
%{_libdir}/libmirisdr.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libmirisdr.pc

%if %{build_docs}
%files devel-doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html
%{_docdir}/%{name}/pdf
%endif


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.0.20130608-alt1_9
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.0.20130608-alt1_7
- fixed build

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.20130608-alt1_5
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.20130608-alt1_3
- new version

