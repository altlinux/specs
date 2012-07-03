Name: alterator-perl-functions
Version: 0.4
Release: alt4

Requires:  gettext
Provides: perl-Alterator-Backend3
Obsoletes: perl-Alterator-Backend3
Conflicts: alterator < 3.3-alt6

Packager: Vladislav Zavjalov <slazav@altlinux.org>

BuildArch: noarch

Source: Backend3.pm

Summary: helper functions for alterator perl based backends
License: GPL
Group: Development/Perl

%description
helper functions for alterator perl based backends

%install
%__install -Dpm0644 %SOURCE0 %buildroot%perl_vendor_privlib/Alterator/Backend3.pm

%files
%perl_vendor_privlib/*

%changelog
* Fri Nov 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt4
- export $LANGUAGE

* Tue Jul 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt3
- add write_enum_item

* Tue Jul 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt2
- add write_debug function

* Mon Jul 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt1
- add validate_symbol function

* Mon Jul 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt6
- function _() can get non-standart po-domain as second argument

* Tue Jun 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt5
- fix write_auto_named_list

* Mon Jun 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt4
- add write_auto_param, write_auto_named_list
- modify write_error
- fix N_ -> _ modification

* Mon Jun 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt3
- change xgettext keyword for perl backends: N_ -> _
- Conflicts: alterator < 3.3-alt6
- some changes in output functions

* Fri May 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt2
- modify output functions

* Thu May 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- simplified version without fork()

* Wed May 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt1
- redirect STDOUT->STDERR in backend; provides custom functions for output instead.
  version with fork()
- add DEBUG var (printing all in and out messages to STDERR)

* Wed May 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt2
- Conflicts: perl-Alterator-Backend3 -> Provides/Obsoletes

* Tue May 27 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt1
- Initial verion. Package perl-Alterator-Backend3 was used...

