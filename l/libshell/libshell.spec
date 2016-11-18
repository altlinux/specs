Name: libshell
Version: 0.4.2
Release: alt1

Summary: A library of shell functions
License: GPL
Group: Development/Other
BuildArch: noarch
Packager: Alexey Gladkov <legion@altlinux.ru>

Url: https://github.com/legionus/libshell.git

Source: %name-%version.tar

BuildRequires: help2man md2man

%description
This package contains common functions for shell projects to increase code reuse.

%package single
Summary: A library of shell functions (single file)
Group: Development/Other

%description single
This package contains common functions for shell projects to increase code reuse
as single file.

%package -n cgrep
Epoch: 1
Summary: Simple program output colorifer
Group: Text tools

%description -n cgrep
This package contains simple wrapper to colorize output from any programs.

%prep
%setup -q

sed -i -e 's,^#!/bin/ash,#!/bin/sh,' \
	utils/cgrep.in

%build
%make

%install
%make_install DESTDIR=%buildroot install
%make_install DESTDIR=%buildroot install-single

%check
%make check

%files
/bin/*
%exclude /bin/shell-lib
%_man3dir/*
%_datadir/%name
%doc COPYING

%files single
/bin/shell-lib

%files -n cgrep
%_bindir/*
%_man1dir/*

%changelog
* Fri Nov 18 2016 Alexey Gladkov <legion@altlinux.ru> 0.4.2-alt1
- New version (0.4.2).
- Add more docs (ALT#17927).
- New utilities:
  + shell-terminfo to simplify work with terminfo.
  + cgrep utility.
- shell-getopt changes:
  + Fix encoding in comment.

* Thu Jun 30 2016 Alexey Gladkov <legion@altlinux.ru> 0.4.1-alt2
- shell-ini-config changes:
  + Preserve file permissions (ALT#32139).

* Tue Nov 24 2015 Alexey Gladkov <legion@altlinux.ru> 0.4.1-alt1
- New version (0.4.1).
- shell-ini-config changes:
  + Return error if config file does not exist (ALT#31151).
- shell-getopt changes:
  + Fix getopt option completion (ALT#31480).

* Sat May 30 2015 Alexey Gladkov <legion@altlinux.ru> 0.4.0-alt1
- New version (0.4.0).
- New utilities:
  + shell-git-config: New functions to read/write git-config-like config files.
- shell-getopt changes:
  + Detect ambiguous long options properly (break compatibility).

* Tue Feb 24 2015 Alexey Gladkov <legion@altlinux.ru> 0.3.0-alt1
- New version (0.3.0).
- Fix bootstrap (ALT#29584).
- shell-ini-config changes:
  + Add ini_config_is_set() function.
  + Take care about lines without values (ALT#30713).
- shell-unittest changes:
  + Add TESTCASES variable to list individual testcases (ALT#27059).
  + Add TESTTRACE variable to run testcase in debug mode (ALT#27059).

* Fri Nov 08 2013 Alexey Gladkov <legion@altlinux.ru> 0.2.0-alt1
- shell_var_trim: Check for empty string (ALT#29562).
- Add missing sources.

* Thu Nov 07 2013 Alexey Gladkov <legion@altlinux.ru> 0.1.9-alt1
- Add functions to daemonize process.
- Add logger support.
- Reimplement shell_var_trim function (ALT#29557).

* Wed Nov 14 2012 Alexey Gladkov <legion@altlinux.ru> 0.1.8-alt1
- shell-ini-config changes:
  + Fix empty lines at EOF (ALT#27974).
  + Indentation in the ini-file can be configured by
    shell_ini_config_prefix (ALT#27915).

* Sun Apr 01 2012 Alexey Gladkov <legion@altlinux.ru> 0.1.7-alt1
- Packaged -single subpackage with all libshell functions bundled into
  the single shell-lib file.
- New utilities:
  + shell-cmdline: New functions to parse /proc/cmdline.
- shell-error changes:
  + Add optional timestamp to messages.
- shell-run changes:
  + Add SCRIPT_ERROR_FATAL var to control execution interrupt
    on error (thx Ildar Mulyukov).
  + Fix execution order of scripts in run_scripts() (thx Ildar Mulyukov).
- shell-args changes:
  + Add opt_check_exec().
- Other changes:
  + Generate SYMS and DEPS files.

* Wed Jul 27 2011 Alexey Gladkov <legion@altlinux.org> 0.1.6-alt1
- shell-ini-config changes (ALT#25946):
  + Fix comment formatting (thx Vladislav Zavjalov);
  + Add section if it is not exists (thx Vladislav Zavjalov);
  + Fix error at adding values to the last section (thx Vladislav Zavjalov);
  + Fix error of adding values into incorrect sections (thx Vladislav Zavjalov).

* Sun May 15 2011 Alexey Gladkov <legion@altlinux.ru> 0.1.5-alt1
- shell-quote changes:
  + Fix depends.
- shell-var changes:
  + Fix depends.
  + Fix shell_var_unquote function.
- shell-ini-config changes:
  + Rewrite all functions in shell.
- Other changes:
  + Update tests.
- Spec:
  + Add check section.

* Wed Nov 03 2010 Alexey Gladkov <legion@altlinux.org> 0.1.4-alt1
- shell-signal changes:
  + Fix return status and rewrite tests.
- shell-source changes:
  + Remove bashisms.
  + Reduce size of internal function.
- Other changes:
  + contrib: CRC32 implementation.

* Thu Apr 29 2010 Alexey Gladkov <legion@altlinux.ru> 0.1.3-alt1
- shell-signal: Reimplement signal_handler function.
- shell-ip-address: Add ipv4_ip_subnet, ipv4_mask2prefix and
  ipv4_prefix2mask functions.

* Tue Nov 17 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.2-alt1
- shell-unittest: Increase performance.
- shell-unittest: Allow to set unittest_show_condition variable
  prior to executing test-running
- shell-ip-address: Fix unbound variable.
- shell-mail-address: .travel TLD is lost when shell_mail_address_strict is unset.
- shell-getopt: Fix for FreeBSD-7.2.

* Thu Oct 08 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.1-alt1
- New utilities:
  + shell-run: New functions to scripts from directory.
  + shell-source: New functions to source shell code under some conditions.
- shell-quote changes:
  + Allow \t as delimiter.
- Other changes:
  + Protect IFS variable when 'set --' executing.

* Fri Apr 24 2009 Alexey Gladkov <legion@altlinux.org> 0.1.0-alt2
- Fix shell-var installation.

* Wed Apr 15 2009 Alexey Gladkov <legion@altlinux.org> 0.1.0-alt1
- New utilities:
  + shell-var: New functions to handle shell parameters.
- shell-quote changes:
  + Major changes in quote_shell_args().
  + Rewrite quote_shell_args() from scratch, to avoid the dangerous
    shell constructions.
  + Fix Usage for quote_shell_args.
  + Add quote_shell_args().
- shell-unittest changes:
  + Add default comment initialization.
- shell-args changes:
  + parse_common_option(): Option --quiet cancels option --verbose.
- Other changes:
  + Update COPYING.
  + UnitTest: Add tests for quote_shell_args() function.
  + shell_var_unquote(), string_quote_remove(): Fix "'" unquote
    for bash.

* Fri Feb 27 2009 Alexey Gladkov <legion@altlinux.org> 0.0.9-alt2
- shell*-config changes:
  + Fix dependency.

* Thu Feb 19 2009 Alexey Gladkov <legion@altlinux.org> 0.0.9-alt1
- shell-getopt changes:
  + preserves the options order.
- Other changes:
  + Add .gear/changelog file.
  + contrib/shell-sort: Implementation of sorting the array.
  + contrib/shell-array: Reimplement arrays.

* Wed Dec 03 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.8-alt1
- shell-getopt changes:
  + Fix regression.
- Other changes:
  + shell-quote: *_variable(): Fix internal namespace.
  + Add tests for quote_sed_regexp_variable() and
    quote_shell_variable().

* Sun Nov 30 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.7-alt1
- shell-getopt changes:
  + getopt(): OPTIND should be local.
  + Fix messages compatibility with getopt(1).
- shell-signal changes:
  + signal_handler(): Fix SIG_DFL special action.
  + signal_handler(): Remove SIG prefix from a signal symbolic name.
  + signal_handler(): Fix quoting.
  + module is no longer a experimental.
- shell-quote changes:
  + Add quote_shell_variable() and quote_sed_regexp_variable()
    functions.
  + Use an internal quoting function to avoid unnecessary subshells.
- Documentation changes:
  + libshell.man: Add shell-error.
  + shell-error.man: Add man-page for shell-error.
  + libshell.man: Add libshell man-page.
- Other changes:
  + Add makefile.
  + Add unit tests for shell-signal.

* Mon Sep 29 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.6-alt1
- New utilities:
  + shell-ini-config: New functions to read/write
    ini-like config files.
  + shell-signal: Add signal handling functions (experimental).
- shell-getopt changes:
  + Add env variables desciption.
- shell-unittest changes:
  + registerTests argument is optional.
  + assertTrue() and assertFalse() should always display message
    if test failed.
  + Add new function to able register test functions automatically.
  + appendTests(): test function could be registered only once.
  + Add unittest_show_condition parameter.
  + runUnitTests should return 1 if some tests has failed.
- shell-ip-address changes:
  + Add regular expression to IP address validation.

* Thu Jun 05 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt1
- Add shell-unittest for writing Unit tests.

* Wed May 28 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.4-alt1
- Add shell-ip-address to IP address validation;
- Add shell-mail-address to mail address validation;
- shell-getopt:
  + Handle first '-' in short options;
  + Fix POSIXLY_CORRECT mode.

* Thu Mar 13 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.3-alt1
- shell-getopt: getopt():
  + Add --alternative handle;
  + Allow empty arguments;
  + Improve getopt(1) compatibility;
  + Ignore first '-' in options.
- shell-config:
  + Add shell_config_del() and shell_config_comment() functions.

* Sun Mar 09 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.2-alt4
- shell-getopt: Move getopt(), getsubopt(), getopts() and getoptex()
  from experimental state.
- shell-quote: Move string_quote_remove() from experimental state.

* Wed Feb 27 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.2-alt2
- shell-config: shell_config_set():
  + Fix value quoting.
- shell-getopt: getopt():
  + Fix GETOPT_ALLOW_UNKNOWN=1;
  + Fix return codes;
  + Fix params handling.

* Fri Feb 22 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.2-alt1
- Add shell-version to trac API changes.
- Add shell-getopt. This is getopts(1), getopt(1) and getsubopt(3)
  shell implementation (if __libshell_experimental is set).
- Rename shell-regexp to shell-quote.
- shell-quote:
  + Add string_quote_remove() to remove ' or " symbols from start
  and end of string (if __libshell_experimental is set).
  + Remove unquote_sed_regexp(), unquote_shell() functions.

* Mon Jan 28 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt4
- Add shell-config to read and write shell-like config files:
  + shell-config: shell_config_get() read value from config file;
  + shell-config: shell_config_set() change or write value
    to config file;
- shell-args:
  + opt_check_read(), opt_check_dir() Fix error message.
- shell-regexp:
  + Add new functions: unquote_sed_regexp(), unquote_shell().

* Thu Sep 20 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt3
- Workaround quoting for ash.

* Fri Jul 06 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt2
- shell-error: Rename info() to message().

* Thu Feb 22 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt1
- Initial revision.
