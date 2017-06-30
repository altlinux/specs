Name: ht
Version: 2.1.0
Release: alt1
Summary: Disassembler, object dumper and hex editor
License: GPLv2
Group: Development/Tools
Url: http://hte.sourceforge.net/
Source: %name-%version.tar
Patch1: %name-%version-alt-build.patch

BuildRequires: flex gcc-c++ liblzo2-devel libncursesw-devel libX11-devel xorg-xproto-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
HT is a file editor/viewer/analyzer for executables. The goal is to combine
the low-level functionality of a debugger and the usability of IDEs.


%prep
%setup -q
%patch1 -p1


%build
%configure
%make_build CC=%__cc CXX=%__cxx CFLAGS="%optflags" CXXFLAGS="%optflags"
gzip -9c ChangeLog > ChangeLog.gz


%install
%makeinstall_std
install -pD -m 0644 {doc,%buildroot%_infodir}/%name.info


%files
%doc AUTHORS ChangeLog.* KNOWNBUGS README TODO doc/*.html
%_bindir/*
%_infodir/*


%changelog
* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Updated to version 2.1.0

* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.22-alt1.2
- Fix build with gcc6

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.22-alt1.1
- NMU: added BR: texinfo

* Wed Feb 05 2014 Led <led@altlinux.ru> 2.0.22-alt1
- initial build
