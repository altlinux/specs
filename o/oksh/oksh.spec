%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: oksh
Version: 7.5
Release: alt1

Summary: Portable OpenBSD ksh(1)
License: Unlicense and BSD and ISC
Group: Shells

URL: https://github.com/ibara/oksh
# https://github.com/ibara/oksh/releases/download/oksh-%version/oksh-%version.tar.gz
Source: %name-%version.tar
Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildRequires: libncurses-devel

%description
Self-contained port of OpenBSD's ksh(1) aimed to be maximally portable
across operating systems and C compilers.

%prep
%setup

%build
%configure --enable-curses --no-strip
%make_build

%install
%makeinstall_std

%files
%doc CONTRIBUTORS NOTES README.md README.pdksh
%_bindir/oksh
%_man1dir/oksh.1*

%changelog
* Thu May 30 2024 Aleksey Cheusov <cheusov@altlinux.org> 7.5-alt1
- 7.5-alt1

* Sun Dec  5 2021 Aleksey Cheusov <cheusov@altlinux.org> 7.0-alt2
- Do not set set_verify_elf_method macros

* Sun Dec  5 2021 Aleksey Cheusov <cheusov@altlinux.org> 7.0-alt1
- Update

* Thu May 21 2020 Aleksey Cheusov <cheusov@altlinux.org> 6.7-alt2
- Fix licence and improve changelog

* Wed May 20 2020 Aleksey Cheusov <cheusov@altlinux.org> 6.7-alt1
- Initial packaging
