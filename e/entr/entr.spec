Name:    entr
Version: 5.6
Release: alt1

Summary: Event Notify Test Runner
License: ISC
Group:   Other
Url:     https://github.com/eradman/entr.git

Source: %name-%version.tar

#BuildRequires: file pgrep git vim tmux

%description
A utility for running arbitrary commands when files change. Uses kqueue(2) or
inotify(7) to avoid polling.  `entr` was written to facilitate rapid feedback
on the command line.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std PREFIX=/usr

%check
%make_build test

%files
%doc *.md LICENSE
%_bindir/*
%_man1dir/*

%changelog
* Thu Jul 04 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.6-alt1
- 5.6

* Fri Dec 01 2023 Andrew A. Vasilyev <andy@altlinux.org> 5.5-alt1
- 5.5

* Sat Aug 26 2023 Andrew A. Vasilyev <andy@altlinux.org> 5.4-alt1
- Initial build for ALT.

