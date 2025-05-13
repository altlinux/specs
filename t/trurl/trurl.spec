%def_with check

Name:    trurl
Version: 0.16.1
Release: alt1

Summary: trurl is a command line tool for URL parsing and manipulation
License: curl
Group:   Text tools
Url:     https://curl.se/trurl
Vcs:     https://github.com/curl/trurl

Source: %name-%version.tar

BuildRequires: pkgconfig(libcurl)
%if_with check
BuildRequires: python3
%endif

%description
%summary.

%prep
%setup
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' Makefile
%endif

subst \
's!$(ZSH_COMPLETIONSDIR)/_trurl;!$(DESTDIR)$(ZSH_COMPLETIONSDIR)/_trurl;!g' \
Makefile

%build
%make_build PREFIX=%_prefix
%make completions

%install
%makeinstall_std PREFIX=%_prefix \
COMPLETION_FILES='completions/_trurl.zsh'

%check
%make test

%files
%doc COPYING RELEASE-NOTES THANKS
%_bindir/%name
%_man1dir/%name.1.*
%_datadir/zsh/site-functions/_%name

%changelog
* Tue May 13 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.16.1-alt1
- 0.16 -> 0.16.1

* Thu Oct 10 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.16-alt1
- 0.14 -> 0.16

* Sat Aug 10 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.14-alt2
- Fixed build for Elbrus

* Mon Aug 05 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.14-alt1
- Initial build for Sisyphus
