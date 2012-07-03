# Generated File.
%setup_docs_module maintainer_howto ru

Name: %packagename
Version: 0.3.1
Release: alt1

Summary: ALT Linux Team Novice Maintainer HOWTO
Summary(ru_RU.KOI8-R): Руководство начинающего мантейнера ALT Linux Team
License: %fdl
Url: http://heap.altlinux.ru/kirill/maintainer_howto/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# rename: docs-maintainer_howto-kirill -> docs-maintainer_howto
Provides: docs-maintainer_howto-kirill = 060413-alt1
Obsoletes: docs-maintainer_howto-kirill <= 060413-alt1

Source: %name-%version.tar

%description
This HOWTO is aimed to help those who want to join ALT Linux Team as a Sisyphus package maintainer.

%description -l ru_RU.KOI8-R
Документ для тех, кто хочет присоединиться к ALT Linux Team и стать мантейнером Sisyphus.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "maintainer.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Jun 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3.1-alt1
- changes from ldv@
  + allow and recommend RSA 2048 keys for openssh

* Thu Jan 31 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- fixed inaccuracy: (thanks ldv@)
  + s/Security Officer/ALT Security Team/
  + s/cvs.altlinux.org/devel.altlinux.org/
  + Deprecate non-source packages
  + Update rsync invocation and output

* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- fixed example and real e-mails
  + brought e-mails into compliance with current policy
- added ssh-keygen example command / reformatted gpg --export example
- fixed typos

* Thu Jan 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed:
  + docs-maintainer_howto-kirill -> docs-maintainer_howto
- used %fdl macro for License tag
- build against rpm-build-docs-experimental

* Wed Apr 19 2006 Kirill Maslinsky <kirill@altlinux.ru> 060413-alt1
- Initial build for Sisyphus.

