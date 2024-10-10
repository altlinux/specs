%def_with check

Name:    trurl
Version: 0.16
Release: alt1

Summary: trurl is a command line tool for URL parsing and manipulation
License: curl
Group:   Text tools
Url:     https://curl.se/trurl
Vcs:     https://github.com/curl/trurl

Source0: %name-%version.tar
Source1: %name.1

BuildRequires: pkgconfig(libcurl)
%if_with check
BuildRequires: python3
%endif

%description
%summary.

%prep
%setup
cp -av %SOURCE1 .

%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' Makefile
%endif

%build
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%check
%make test

%files
%doc *.md
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Thu Oct 10 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.16-alt1
- 0.14 -> 0.16

* Sat Aug 10 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.14-alt2
- Fixed build for Elbrus

* Mon Aug 05 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.14-alt1
- Initial build for Sisyphus
