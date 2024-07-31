Name: hackbrowserdata
Version: 0.4.6
Release: alt1

Summary: Command-line tool for decrypting and exporting browser data

License: MIT
Group: Development/Tools
Url: https://github.com/moonD4rk/HackBrowserData

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang

ExclusiveArch: %go_arches

BuildRequires: golang >= 1.19
Provides: HackBrowserData

%description
HackBrowserData is a command-line tool for decrypting and exporting browser data
(passwords, history, cookies, bookmarks, credit cards, download history,
localStorage and extensions) from the browser.
It supports the most popular browsers on the market and runs on Windows, macOS and Linux.

%prep
%setup

%build
pushd cmd/hack-browser-data
CGO_ENABLED=1 go build -mod=vendor
popd

%install
mkdir -p %buildroot%_bindir
install -m755 cmd/hack-browser-data/hack-browser-data  %buildroot/%_bindir/hack-browser-data

%files
%doc README.md
%_bindir/hack-browser-data

%changelog
* Wed Jul 31 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.4.6-alt1
- v0.4.6

* Mon Feb 19 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.4.5-alt1
- Initial build for ALT.
