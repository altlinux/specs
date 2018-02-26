%setup_docs_module install_junior ru

Name: %packagename
Version: 0.4.2
Release: alt1

Summary: ALT Linux Junior Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке ALT Linux Junior
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# rename: docs-install-junior -> docs-install_junior
Provides: docs-install-junior = 0.1-alt3
Obsoletes: docs-install-junior <= 0.1-alt3

Source: %name-%version.tar

%description
ALT Linux Junior Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке ALT Linux Junior.

%prep
%setup

%build
%docs_module_build "m-k" "index.m-k"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Fri Jun 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.2-alt1
- fixes from bertis@:
  + minorly edited (style and structure)
  + one typo fixed

* Fri Mar 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.1-alt1
- fixed directory tree description needed for netinstall

* Sat Mar 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- typo and punctuation fixes (thanks bertis@)
- removed one more smc(www) mention

* Wed Mar 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- moved bootloader section to its proper place

* Wed Mar 05 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- step names are links now

* Thu Feb 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- package renamed: docs-install-junior -> docs-install_junior
- more detailed netinstall description (#14250)

* Mon Jan 28 2008 Vladimir Zhukov <bertis@altlinux.ru> 0.1-alt3
- package rebuilt
  + fixed missing heading & screenshot (closes #14193)

* Wed Dec 19 2007 Vladimir Zhukov <bertis@altlinux.ru> 0.1-alt2
- package rebuilt
  + synchronized with latest junior installer (2007.12.17)

* Fri Nov 23 2007 Vladimir Zhukov <bertis@altlinux.org> 0.1-alt1
  - initial build
    spec based on docs-install-desktop_lite.spec

