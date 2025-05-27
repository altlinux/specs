Name: scc
Version: 3.5.0
Release: alt1
Summary: Sloc, Cloc and Code. Count lines of code.
License: MIT
Group: File tools
URL: https://github.com/boyter/scc

Source: %name-%version.tar

BuildRequires: golang >= 1.21
BuildRequires(pre): rpm-build-golang

%global gobuild_is_noarch 0

%description
scc is a very fast accurate code counter focusing on complexity.
It can count lines of code (SLOC) and estimate code complexity for
a large number of programming languages.

%prep
%setup -q -n %name-%version

%build
export LDFLAGS="-buildmode=pie -X main.Version=%version"
%gobuild .

%install
install -Dpm 0755 ./%name %buildroot%_bindir/%name

%files
%doc README.md
%doc LICENSE
%_bindir/%name

%changelog
* Mon May 26 2025 Valery Sinelnikov <greh@altlinux.org> 3.5.0-alt1
- Initial build for ALT Linux

