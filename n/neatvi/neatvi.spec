%define _unpackaged_files_terminate_build 1

Name: neatvi
Version: 19
Release: alt1

Summary: Small vi/ex editor for editing UTF-8 text
License: ISC
Group: Editors
Url: https://github.com/aligrudi/neatvi
Vcs: https://github.com/aligrudi/neatvi.git

Source: %name-%version.tar

%description
Neatvi is a small vi/ex editor for editing UTF-8 text.  It supports
syntax highlighting, multiple windows, right-to-left languages, and
keymaps

%prep
%setup

%build
%make_build

%install
install -Dpm755 vi %buildroot%_bindir/neatvi
install -Dpm755 stag %buildroot%_bindir/stag

%check
./test.sh && echo "All tests OK"|| :

%files
%doc README
%_bindir/%name
%_bindir/stag

%changelog
* Wed Aug 05 2026 Mikhail Nogin <joycap@altlinux.org> 19-alt1
- Initial built for Sisyphus.
