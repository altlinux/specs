%global import_path github.com/Owloops/updo

Name: updo
Version: 0.4.7
Release: alt1

Summary: Uptime monitoring CLI tool
License: MIT
Group: Other

Url: https://github.com/Owloops/updo
Vcs: https://github.com/Owloops/updo

Packager: Aleksandr Shamaraev <shad@altlinux.org>

Source0: %name-%version.tar
Source1: vendor.tar
Source2: vendor2.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang zip

%description
Uptime monitoring CLI tool with alerting and advanced settings.

%prep
%setup -a1

tar -xf %SOURCE2 -C lambda/

subst 's|dev|%version|' main.go
subst 's|unknown||' main.go

rm aws/bootstrap.zip

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path/lambda
GOOS=linux GOARCH=arm64 CGO_ENABLED=0 go build -tags lambda.norpc -ldflags="-s -w" -o ../aws/bootstrap $(notdir lambda/lambda.go)
cd ..
cd aws && zip -q bootstrap.zip bootstrap

cd %_builddir/%name-%version/.build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md LICENSE
%_bindir/*

%changelog
* Wed Apr 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.4.7-alt1
- 0.4.6 -> 0.4.7

* Fri Feb 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.4.6-alt1
- 0.4.5 -> 0.4.6

* Mon Dec 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.5-alt1
- 0.4.4 -> 0.4.5

* Tue Oct 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.4-alt1
- 0.4.3 -> 0.4.4

* Tue Aug 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt1
- 0.4.2 -> 0.4.3

* Sat Aug 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.2-alt1
- 0.4.1 -> 0.4.2

* Fri Aug 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1

* Tue Aug 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.0-alt1
- 0.3.8 -> 0.4.0

* Sat Aug 09 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.8-alt1
- 0.3.4 -> 0.3.8

* Wed Aug 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.4-alt1
- 0.3.1 -> 0.3.4

* Mon Aug 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.1-alt1
- 0.2.7 -> 0.3.1

* Wed Jul 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.7-alt1
- 0.2.3 -> 0.2.7

* Thu Jun 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.3-alt1
- 0.2.2 -> 0.2.3

* Wed Jun 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.2-alt1
- 0.1.8 -> 0.2.2

* Tue Jun 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.8-alt1
- 0.1.7 -> 0.1.8

* Thu May 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.7-alt1
- 0.1.5 -> 0.1.7

* Wed May 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.5-alt1
- 0.1.2 -> 0.1.5

* Mon Apr 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.2-alt1
- Initial build for ALT Linux.
