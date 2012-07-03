%define _altdata_dir %_datadir/alterator

Name: alterator-sh-functions
Version: 0.13
Release: alt3

Requires: gettext libshell >= 0.1.0-alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

Summary: helper functions for alterator shell based backends
License: GPL
Group: System/Base

BuildPreReq: libshell >= 0.1.0-alt2

Conflicts: alterator < 3.4-alt1

%description
helper functions for alterator shell based backends

%prep
%setup -q

%build
%make check

%install
%makeinstall

%files
%_bindir/*
%_man3dir/*

%changelog
* Mon Dec 27 2010 Vladislav Zavjalov <slazav@altlinux.org> 0.13-alt3
- file_list_add(): use "fgrep -x" instead of "fgrep -w"

* Mon Nov 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.13-alt2
- fix procedure call (avoid second call during type request)

* Fri Nov 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.13-alt1
- add support of alterator_export_proc()

* Thu Nov 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.12-alt1
- add support of alterator_export_var()

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.11-alt2
- use shell-var library.
- add helper functions to simplify file list manipulations.

* Tue Apr 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.11-alt1
- add write_blob_param function

* Mon Apr 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.10-alt6
- add man page

* Wed Feb 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt5
- fix run_localized()

* Wed Feb 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt4
- add run_localized() and use it in _()

* Tue Feb 10 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt3
- don't cut spaces from backend input

* Mon Feb 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt2
- resurrect write_language() function; don't eval set_locale

* Fri Feb 06 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt1
- add set_locale function

* Fri Dec 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt3
- fix alterator-sh-functions to works with backends using sh -u
  (work with undefined ALTERATOR_DEBUG)

* Wed Dec 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt2
- fix alterator-sh-functions to works with backends using sh -u
- move exec 1>&2 to message_loop()
  (now you may set alterator_api_version after including alterator-sh-functions)

* Fri Nov 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- fix library file permissions
- write_debug: use ALTERATOR_DEBUG environment variable instead of DEBUG

* Thu Oct 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt3
- don't quote booleans in write_table_item (by aspsk@)

* Thu Oct 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- minimize library deps

* Fri Oct 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- add assertList

* Tue Sep 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- add alterator-unittest-functions

* Fri Sep 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt5
- add write_type_item function
- run unit-tests with '-e'

* Fri Sep 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt4
- protect from double loading (avoiding problems with io redirections)

* Tue Jul 01 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- add default po_domain value

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- fix write_enum function (should write to >&3)
- more tests (for output channel)
- move string and symbol testcases to common library

* Wed Jun 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- add write_table_item function
- add write_debug function
- split write_enum_item into  write_enum_item (for command args) and write_enum (for stream)
- add new testcase (empty name)
- fix string test

* Fri Jun 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- more tests for public read and write api
- minor improvements in code:
  * move variables resetting (reset on message start)
  * move userhandler to private area

* Thu Jun 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- more tests for public write api
- minor bugfixes in code:
  * _write_begin and _write_end now internal helpers
  * add parameter name validation

* Thu Jun 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- add first unit-tests (quote and unquote)

* Wed Jun 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- write_enum_item: write without implicit name attribute

* Thu May 29 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- alterator_api_version=1:
    * protect stdout from unexpected output
    * hide start and end markers output ( '(' and ')' )

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- add write_bool_param function

* Tue May 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- add write_string_param function

* Tue May 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- optimize write_string function (thanks to legion@)
- add write_enum_item function

* Thu Mar 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- improve string_quote function

* Tue Feb 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- fix '_' function: 
    gettext utility uses encoding from LC_CTYPE and translation from LANGUAGE

* Wed Jan 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- requires gettext
- new function: test_bool

* Mon Jan 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
