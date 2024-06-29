%define _upver 1.3.4
%define _datever 20240622

Name: mawk
Version: %_upver.%_datever
Release: alt1

Summary: Implementation of New/POSIX AWK
License: GPLv2+
Group: Text tools

URL: http://invisible-island.net/mawk/mawk.html
# ftp://ftp.invisible-island.net/mawk/mawk-%{_upver}-%{_datever}.tgz
Source: %name-%version.tar

%description
mawk is an interpreter for the AWK Programming Language. It implements the AWK
language as defined in Aho, Kernighan and Weinberger, The AWK  Programming
Language, Addison-Wesley Publishing, 1988. Furthermore, it conforms to the
POSIX 1003.2 (draft 11.3) definition of the AWK language and additionally
provides a small number of extensions.

%package doc
Summary: Documentation for mawk
Group: Development/Documentation
BuildArch: noarch

%description doc
This package contains examples for mawk.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc README ACKNOWLEDGMENT CHANGES
%_bindir/mawk
%_man1dir/mawk.1*

%files doc
%doc examples/

%changelog
* Sat Jun 29 2024 Aleksey Cheusov <cheusov@altlinux.org> 1.3.4.20240622-alt1
- 1.3.4-20240622

* Thu May 30 2024 Aleksey Cheusov <cheusov@altlinux.org> 1.3.4.20240123-alt1
- 1.3.4.20240123

* Wed May 20 2020 Aleksey Cheusov <cheusov@altlinux.org> 1.3.4.20200120-alt3
- Minor clean-ups for spec

* Tue May 19 2020 Aleksey Cheusov <cheusov@altlinux.org> 1.3.4.20200120-alt2
- Fix Group and License

* Tue May 19 2020 Aleksey Cheusov <cheusov@altlinux.org> 1.3.4.20200120-alt1
- 1.3.4-20200120

* Tue May 19 2020 Aleksey Cheusov <cheusov@altlinux.org> 1.3.4.20171017-alt1
- Initial packaging for AltLinux
