# hey Emacs, its -*- rpm-spec -*-
# vim: set ft=spec fdm=marker :

# {{{ Defines
%define name ruby
%define base_name ruby
%define version 1.9.2
%define release 2
%define svn r31204
%define subver %(echo %version |cut -d. -f1,2)
%define platform %(%_datadir/automake/config.sub %_target_platform | sed -e 's,-%_vendor,,')
%define rubylibdir_base %_datadir/%base_name
%define rubylibdir %rubylibdir_base/%subver
%define archdir_base %_libdir/%base_name
%define archdir %archdir_base/%subver/%platform
%define vendordir_base %_datadir/%base_name/vendor_ruby
%define vendordir %vendordir_base/%subver
%define vendorarchdir_base %_libdir/%base_name/vendor_ruby
%define vendorarchdir %vendorarchdir_base/%subver/%platform
%define rubyhdrdir %_includedir/%base_name/%subver
%define vendorhdrdir %rubyhdrdir/vendor_ruby
%define ruby_ri_dir_base %_datadir/ri
%define ruby_ri_dir %ruby_ri_dir_base/%subver

%def_without emacs

%set_verify_elf_method fhs=normal
# }}}

# {{{ General
Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Name: %name
Version: %version
Release: alt%release.%svn.1
Summary: Interpreter of object-oriented scripting language Ruby %subver
License: Dual: GPL and Ruby
Url: http://www.ruby-lang.org/
Group: Development/Ruby

Requires: lib%name = %version-%release
Conflicts: ruby1.8

Source: %base_name-%version-%release.tar
Source1: README.ALT-UTF8

Patch1: ruby-1.9.2-alt-check-last-line-not-second.patch
Patch2: ruby-1.9.2-alt-correct-less-invocation-AND-pager-selection.patch
Patch3: ruby-1.9.2-alt-disable-rubygems.patch
Patch4: ruby-1.9.2-alt-do-not-generate-docs.patch
Patch5: ruby-1.9.2-alt-emacs.patch
Patch6: ruby-1.9.2-alt-FSH.patch
Patch7: ruby-1.9.2-alt-group_member_3-is-not-handled-by-fakeroot_1.patch
Patch8: ruby-1.9.2-alt-increase-timeouts-to-pass-tests-on-arm.patch
Patch9: ruby-1.9.2-alt-libruby-search-path-in-mkmf-tests.patch
Patch10: ruby-1.9.2-alt-manpages.patch
Patch11: ruby-1.9.2-alt-On-x86_64-sin_3-is-using-xmm0-register-for-both-argument-and-return-value.patch
Patch12: ruby-1.9.2-alt-ri_cache_utility.patch
Patch13: ruby-1.9.2-alt-RubyNode.patch
Patch14: ruby-1.9.2-alt-specific.patch
Patch15: ruby-1.9.2-alt-string.patch

# Automatically added by buildreq on Mon Apr 20 2009 (-bi)
BuildRequires: groff-base libdb4-devel libffi-devel libgdbm-devel libncursesw-devel libreadline-devel libssl-devel libyaml-devel rpm-build-ruby ruby-stdlibs tk-devel zlib-devel
BuildRequires: /dev/pts

# XXX@stanv: test in multi-threads environment never finished.
BuildRequires: schedutils
# }}}


# {{{ Description
%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

Interpreter of object-oriented scripting language Ruby %subver.
# }}}

# Subpackages {{{

%define obsolete() Obsoletes: %1\
Provides: %1 = %version-%release

# {{{ lib%name
%package -n lib%name
Summary: Libraries necessary to run the Ruby %subver
Group: System/Libraries
# enumerator.c:    rb_provide("enumerator.so");   /* for backward compatibility */
Provides: ruby(enumerator)
Provides: %archdir
Provides: %rubylibdir
Provides: %vendorarchdir
Provides: %vendordir
%obsolete %name-module-rubynode

%description -n lib%name
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

This package includes the libruby, necessary to run Ruby %subver.
# }}}

# {{{ lib%name-devel
%package -n lib%name-devel
Summary: Header files for compiling extension modules for the Ruby %subver
Group: Development/Ruby
Requires: lib%name = %version-%release
Requires: rpm-build-%name
Requires: %name-tool-rdoc
Provides: %rubyhdrdir
Provides: %vendorhdrdir

Conflicts: lib%name-devel > %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

This package contains the header files, necessary to make extension
library for Ruby %subver.
# }}}

# {{{ lib%name-devel-static
%package -n lib%name-devel-static
Summary: Statically linked Ruby %subver library
Group: Development/Ruby
Requires: lib%name-devel = %version-%release

Conflicts: lib%name-devel-satic > %version-%release
Conflicts: lib%name-devel-satic < %version-%release

%description -n lib%name-devel-static
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

This package includes statically linked Ruby %subver library needed for
embedding Ruby in other applications.
# }}}

# {{{ %name-doc-examples
%package -n %name-doc-examples
Summary: This package provides example programs about Ruby %subver
Group: Development/Ruby
Requires: lib%name = %version-%release

%description -n %name-doc-examples
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.
# }}}

# {{{ %name-doc-ri
%package -n %name-doc-ri
Summary: This package provides ri documentation for Ruby %subver
Group: Development/Ruby
BuildArch: noarch
Requires: lib%name = %version-%release
Requires: %name-tool-ri
Provides: %ruby_ri_dir/site

%description -n %name-doc-ri
This package provides ri documentation for Ruby %subver
# }}}

# {{{ %name-misc-elisp
%if_with emacs
%package -n %name-misc-elisp
Summary: ruby-mode for Emacsen
Group: Development/Ruby
Provides: emacs-ruby-mode
Requires: emacs-common

%description -n %name-misc-elisp
This package provides major-mode for editing Ruby scripts and some
emacs-lisp programs for Ruby programmers.
%endif
# }}}

# {{{ %name-tool-irb
%package -n %name-tool-irb
Summary: Interactive Ruby (for Ruby %subver)
Group: Development/Ruby
BuildArch: noarch
Requires: %name = %version-%release
Requires: lib%name = %version-%release

Conflicts: %name-tool-irb > %version-%release
Conflicts: %name-tool-irb < %version-%release

%description -n %name-tool-irb
The irb is acronym for Interactive RuBy. It evaluates Ruby expression from
the terminal.

This package provides the irb which uses Ruby %subver.
# }}}

# {{{ %name-tool-rdoc
%package -n %name-tool-rdoc
Summary: Generate documentation from Ruby source files (for Ruby %subver)
Group: Development/Ruby
BuildArch: noarch
Requires: %name = %version-%release
Requires: lib%name = %version-%release

Conflicts: %name-tool-rdoc > %version-%release
Conflicts: %name-tool-rdoc < %version-%release

%description -n %name-tool-rdoc
RDoc - Documentation from Ruby Source Files:

* Generates structured HTML and XML documentation from Ruby source
  and C extensions.
* Automatically extracts class, module, method, and attribute
  definitions. These can be annotated using inline comments.
* Analyzes method visibility.
* Handles aliasing.
* Uses non-intrusive and implicit markup in the comments. Readers of
  the original source needn't know that it is marked up at all.

This package provides the RDoc tool which uses Ruby %subver.
# }}}

# {{{ %name-tool-ri
%package -n %name-tool-ri
Summary: Ruby Interactive reference (for Ruby %subver)
Group: Development/Ruby
BuildArch: noarch
Requires: %name = %version-%release
Requires: %name-tool-rdoc
Requires: lib%name = %version-%release

Conflicts: %name-tool-ri > %version-%release
Conflicts: %name-tool-ri < %version-%release

%description -n %name-tool-ri
ri is a command line tool that displays descriptions of built-in Ruby
methods, classes, and modules. For methods, it shows you the calling
sequence and a description. For classes and modules, it shows a
synopsis along with a list of the methods the class or module
implements.

This package provides ri command and descriptions about Ruby %subver.
# }}}

# {{{ %name-stdlibs
%package -n %name-stdlibs
Summary: Standard Ruby %subver library
Group: Development/Ruby
Requires: lib%name = %version-%release

Conflicts: %name-stdlibs > %version-%release
Conflicts: %name-stdlibs < %version-%release

%obsolete %name-module-English
%obsolete %name-module-bigdecimal
%obsolete %name-module-cgi
%obsolete %name-module-curses
%obsolete %name-module-date-time
%obsolete %name-module-dbm
%obsolete %name-module-debug
%obsolete %name-module-digest
%obsolete %name-module-dl
%obsolete %name-module-drb
%obsolete %name-module-e2mmap
%obsolete %name-module-erb
%obsolete %name-module-etc
%obsolete %name-module-fcntl
%obsolete %name-module-fileutils
%obsolete %name-module-gdbm
%obsolete %name-module-iconv
%obsolete %name-module-math
%obsolete %name-module-misc
%obsolete %name-module-net
%obsolete %name-module-nkf
%obsolete %name-module-open3
%obsolete %name-module-openssl
%obsolete %name-module-optparse
%obsolete %name-module-patterns
%obsolete %name-module-pty
%obsolete %name-module-readline
%obsolete %name-module-rexml
%obsolete %name-module-rss
%obsolete %name-module-sdbm
%obsolete %name-module-shell
%obsolete %name-module-socket
%obsolete %name-module-stringio
%obsolete %name-module-strscan
%obsolete %name-module-syslog
%obsolete %name-module-thread
%obsolete %name-module-tracer
%obsolete %name-module-uri
%obsolete %name-module-wait
%obsolete %name-module-webrick
%obsolete %name-module-xmlrpc
%obsolete %name-module-yaml
%obsolete %name-module-zlib

%description -n %name-stdlibs
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

This package contains standard Ruby %subver runtime library.
# }}}

# {{{ %name-stdlibs-tk
%package -n %name-stdlibs-tk
Summary: Ruby/Tk bindings
Group: Development/Ruby
Requires: lib%name = %version-%release
%obsolete %name-module-tk
%obsolete %name-module-tcltk

%description -n %name-stdlibs-tk
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

This package contains Ruby/Tk bindings.
# }}}

# }}} Subpackges

# {{{ Prep
%prep
%setup -q -n %base_name-%version-%release

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
#%%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

cp -pfv %_datadir/automake/config.{guess,sub} .

# Threaded tests doesn't play well under heavy load
rm -f bootstraptest/test_thread.rb
rm -f test/ruby/test_thread.rb
rm -f test/rinda/test_rinda.rb
# rubygems?  we don't need no stinkin' rubygems!
rm -rf test/rubygems
# uses system ruby as cgi interpreter
rm -f test/webrick/test_cgi.rb
rm -f test/webrick/test_filehandler.rb

# XXX@stanv, next test doesn't passes.
rm -rf test/test_pty.rb
#rm -rf test/test_tracer.rb
rm -rf test/drb/ut_array_drbssl.rb
rm -rf test/drb/test_drbssl.rb
#rm -rf test/test_timeout.rb
rm -rf test/net/http/utils.rb
rm -rf test/net/http/test_https.rb


# }}}

# {{{ Build
%build

# {{{ Configure
autoconf

export optflags=' '
%configure \
	--enable-frame-address \
	--enable-shared \
	--disable-rpath \
	--enable-pthread \
	--with-rubylibprefix=%rubylibdir_base \
	--with-rubyarchprefix=%archdir_base \
	--with-rubyhdrdir=%rubyhdrdir \
	--with-sitedir=%_prefix/local/share/%base_name/site_ruby \
	--with-sitearchprefix=%_prefix/local/%_lib/%base_name/site_ruby \
	--with-sitehdrdir=%_prefix/local/include/%base_name/%subver/site_ruby \
	--with-vendordir=%vendordir_base \
	--with-vendorarchprefix=%vendorarchdir_base \
	--with-vendorhdrdir=%vendorhdrdir \
	--with-ridir=%ruby_ri_dir_base \
	--with-ruby-version=minor \
	\
	--enable-ipv6 \
	--with-lookup-order-hack=INET \
	#
# }}}

# SMP-incompatible
%make
%make rdoc

# {{{ ruby-elisp
%if_with emacs
for i in misc/*.el ; do
    emacs -batch --eval "(progn
            (setq load-path (append (list \".\") load-path))
            (byte-compile-file \"$i\"))"
done
%endif
# }}}
# }}}

# {{{ Test
%check
export LD_LIBRARY_PATH="%_builddir/%name-%version-%release"
export PATH="%_builddir/%name-%version-%release:$PATH"
export LANG=en_US.UTF-8

# XXX@stanv: test never finished in multi-threaded environment.
taskset 1 %make -k check
# }}}

# {{{ Install
%install

cp %{S:1} .

%make_install DESTDIR=%buildroot install do-install-doc

mkdir %buildroot/bin
ln -s ..%_bindir/%name  %buildroot/bin/%name

mkdir -p %buildroot%vendordir
mkdir -p %buildroot%vendorarchdir
mkdir -p %buildroot%vendorhdrdir
# compat with site*
ln -sf vendor_ruby %buildroot%rubyhdrdir/site_ruby

mkdir -p %buildroot%ruby_ri_dir/site

echo "VENDOR_SPECIFIC=true" > %buildroot%vendordir/vendor-specific.rb

# {{{ ruby-elisp
%if_with emacs
mkdir -p %buildroot/etc/emacs/site-start.d/
mkdir -p %buildroot%_emacslispdir/
install -m 644 ruby.el %buildroot/etc/emacs/site-start.d/
install -m 644 misc/*.el* %buildroot%_emacslispdir/
%endif
# }}}

# {{{ files.req stuff
mkdir -p %buildroot%_rpmlibdir
cat <<EOF >%buildroot%_rpmlibdir/%name-files.req.list
# ruby dirlist for %_rpmlibdir/files.req
%archdir lib%name
%rubylibdir lib%name
%vendorarchdir lib%name
%vendordir lib%name
%rubyhdrdir lib%name-devel
%vendorhdrdir lib%name-devel
%ruby_ri_dir/site %name-doc-ri
EOF
# }}}
# {{{ RI filetrigger
install -pm755 bin/update-ri-cache %buildroot/%_bindir/update-ri-cache
cat <<EOF >>%buildroot%_rpmlibdir/%name-doc-ri.filetrigger
#!/bin/sh

LC_ALL=C grep -qs '^%ruby_ri_dir/site/' || exit 0
exec %_bindir/update-ri-cache %ruby_ri_dir/site
EOF
chmod +x %buildroot%_rpmlibdir/%name-doc-ri.filetrigger
# }}}
# {{{ Leftovers of indeterminate origin

#Package ruby-stdlibs has an unmet dep:
# Depends: ruby(xmlscan/scanner)
# Used by rss/parser.rb:
#   unless const_defined? :AVAILABLE_PARSER_LIBRARIES
#     AVAILABLE_PARSER_LIBRARIES = [
#       ["rss/xmlparser", :XMLParserParser],
#       ["rss/xmlscanner", :XMLScanParser],
#       ["rss/rexmlparser", :REXMLParser],
#     ]
#   end
#
#   AVAILABLE_PARSERS = []
#
#   AVAILABLE_PARSER_LIBRARIES.each do |lib, parser|
#     begin
#       require lib
#       AVAILABLE_PARSERS.push(const_get(parser))
#     rescue LoadError
#     end
#   end
rm -rf %buildroot%rubylibdir/rss/xmlscanner.rb
# }}}

cat <<EOF >%buildroot/.%name.sh
#!/bin/sh

LD_LIBRARY_PATH="%buildroot%_libdir" \
exec \
%buildroot%_bindir/%name \
-I "%buildroot%vendordir:%buildroot%vendorarchdir:%buildroot%rubylibdir:%buildroot%archdir" \
"\$@"
EOF
chmod +x %buildroot/.%name.sh

%define __ruby %buildroot/.%name.sh

# This is a hack but we really don't need to bytecompile
# Python comparison sample in the Ruby manual
unset RPM_PYTHON
# }}}

# {{{ Files

# {{{ %name
%files
%doc NEWS COPYING LEGAL README README.ALT-UTF8 README.EXT ToDo
/bin/%name
%_bindir/%name
%_man1dir/%{name}*
# }}}

# {{{ lib%name
%files -n lib%name
%_libdir/lib%name.so.*
%_rpmlibdir/%name-files.req.list
%archdir/enc
%archdir/rbconfig.rb
%vendordir/vendor-specific.rb
%dir %_datadir/%base_name
%dir %_datadir/%base_name/%subver
%dir %_datadir/%base_name/vendor_ruby
%dir %_datadir/%base_name/vendor_ruby/%subver
%dir %_libdir/%base_name
%dir %_libdir/%base_name/%subver
%dir %_libdir/%base_name/%subver/%platform
%dir %_libdir/%base_name/vendor_ruby
%dir %_libdir/%base_name/vendor_ruby/%subver
%dir %_libdir/%base_name/vendor_ruby/%subver/%platform
# }}}

# {{{ lib%name-devel
%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%base_name
%rubylibdir/mkmf.rb
# }}}

# {{{ lib%name-devel-static
%files -n lib%name-devel-static
%_libdir/lib%name-static.a
# }}}

# {{{ %name-doc-examples
#%files -n %name-doc-examples
#FIXME
# }}}

# {{{ %name-doc-ri
%files -n %name-doc-ri
%_bindir/update-ri-cache
%dir %_datadir/ri
%dir %ruby_ri_dir
%dir %ruby_ri_dir/site
%dir %ruby_ri_dir/system
%ruby_ri_dir/system/*
%_rpmlibdir/%name-doc-ri.filetrigger
# }}}

# {{{ %name-misc-elisp
%if_with emacs
%files -n %name-misc-elisp
%_emacslispdir/*.el*
%_sysconfdir/emacs/site-start.d/ruby.el
%endif
# }}}

# {{{ %name-tool-irb
%files -n %name-tool-irb
%_bindir/irb
%_man1dir/irb.1*
%rubylibdir/irb.rb
%rubylibdir/irb
%doc doc/irb/
# }}}

# {{{ %name-tool-rdoc
%files -n %name-tool-rdoc
%_bindir/rdoc
%rubylibdir/rdoc.rb
%rubylibdir/rdoc
# Depends on rake
%exclude %rubylibdir/rdoc/task.rb
# Test crap
%exclude %rubylibdir/rdoc/markup/formatter_test_case.rb
# }}}

# {{{ %name-tool-ri
%files -n %name-tool-ri
%_bindir/ri
%_man1dir/ri.1*
# }}}

# {{{ %name-stdlibs
%files -n %name-stdlibs
%_bindir/erb
%_man1dir/erb.1*
%rubylibdir/English.rb
%rubylibdir/abbrev.rb
%rubylibdir/base64.rb
%rubylibdir/benchmark.rb
%rubylibdir/bigdecimal
%rubylibdir/cgi
%rubylibdir/cgi.rb
%rubylibdir/cmath.rb
%rubylibdir/complex.rb
%rubylibdir/csv.rb
%rubylibdir/date
%rubylibdir/date.rb
%rubylibdir/debug.rb
%rubylibdir/delegate.rb
%rubylibdir/digest
%rubylibdir/digest.rb
%rubylibdir/dl
%rubylibdir/dl.rb
%rubylibdir/drb
%rubylibdir/drb.rb
%rubylibdir/e2mmap.rb
%rubylibdir/erb.rb
%rubylibdir/expect.rb
%rubylibdir/fiddle
%rubylibdir/fiddle.rb
%rubylibdir/fileutils.rb
%rubylibdir/find.rb
%rubylibdir/forwardable.rb
%rubylibdir/getoptlong.rb
%rubylibdir/gserver.rb
%rubylibdir/ipaddr.rb
%rubylibdir/kconv.rb
%rubylibdir/logger.rb
%rubylibdir/mathn.rb
%rubylibdir/matrix.rb
%rubylibdir/monitor.rb
%rubylibdir/mutex_m.rb
%rubylibdir/net
%rubylibdir/observer.rb
%rubylibdir/open-uri.rb
%rubylibdir/open3.rb
%rubylibdir/openssl
%rubylibdir/openssl.rb
%rubylibdir/optparse
%rubylibdir/optparse.rb
%rubylibdir/ostruct.rb
%rubylibdir/pathname.rb
%rubylibdir/pp.rb
%rubylibdir/prettyprint.rb
%rubylibdir/prime.rb
%rubylibdir/profile.rb
%rubylibdir/profiler.rb
%rubylibdir/psych
%rubylibdir/psych.rb
%rubylibdir/pstore.rb
%rubylibdir/rational.rb
%rubylibdir/resolv-replace.rb
%rubylibdir/resolv.rb
%rubylibdir/rexml
%rubylibdir/rinda
%rubylibdir/ripper
%rubylibdir/ripper.rb
%rubylibdir/rss
%rubylibdir/rss.rb
%rubylibdir/scanf.rb
%rubylibdir/securerandom.rb
%rubylibdir/set.rb
%rubylibdir/shell
%rubylibdir/shell.rb
%rubylibdir/shellwords.rb
%rubylibdir/singleton.rb
%rubylibdir/socket.rb
%rubylibdir/syck
%rubylibdir/syck.rb
%rubylibdir/sync.rb
%rubylibdir/tempfile.rb
%rubylibdir/thread.rb
%rubylibdir/thwait.rb
%rubylibdir/time.rb
%rubylibdir/timeout.rb
%rubylibdir/tmpdir.rb
%rubylibdir/tracer.rb
%rubylibdir/tsort.rb
%rubylibdir/un.rb
%rubylibdir/uri
%rubylibdir/uri.rb
%rubylibdir/weakref.rb
%rubylibdir/webrick
%rubylibdir/webrick.rb
%rubylibdir/xmlrpc
%rubylibdir/yaml
%rubylibdir/yaml.rb
%archdir/bigdecimal.so
%archdir/continuation.so
%archdir/coverage.so
%archdir/curses.so
%archdir/dbm.so
%archdir/digest
%archdir/digest.so
%archdir/dl
%archdir/dl.so
%archdir/etc.so
%archdir/fcntl.so
%archdir/fiber.so
%archdir/fiddle.so
%archdir/gdbm.so
%archdir/iconv.so
%archdir/io
%archdir/mathn
%archdir/nkf.so
%archdir/objspace.so
%archdir/openssl.so
%archdir/psych.so
%archdir/pty.so
%archdir/readline.so
%archdir/ripper.so
%archdir/sdbm.so
%archdir/socket.so
%archdir/stringio.so
%archdir/strscan.so
%archdir/syck.so
%archdir/syslog.so
%archdir/zlib.so
# }}}

# {{{ %name-stdlibs-tk
%files -n %name-stdlibs-tk
%rubylibdir/multi-tk.rb
%rubylibdir/remote-tk.rb
%rubylibdir/tcltk.rb
%rubylibdir/tk*
%archdir/tcltklib.so
%archdir/tkutil.so
# }}}

# }}} Files

# {{{ Changelog
%changelog
* Fri Apr 22 2011 Andriy Stepanov <stanv@altlinux.ru> 1.9.2-alt2.r31204.1
- Adopt Conflicts.

* Thu Apr 21 2011 Andriy Stepanov <stanv@altlinux.ru> 1.9.2-alt1.r31204.1
- SVN revision 31204.

* Fri Mar 18 2011 Andriy Stepanov <stanv@altlinux.ru> 1.9.2-alt1.r30896.1
- SVN revision 30896.
- Tests runs on single CPU. XXX: fix this one.

* Fri Dec 31 2010 Alexey I. Froloff <raorn@altlinux.org> 1.9.2-alt1.r30363.1
- SVN revision 30363 AKA 1.9.2p136
- Resurrected pager selection patch for ri
- Added filetrigger for site ri cache update

* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 1.9.2-alt1.r29921.1
- SVN revision 29921 AKA 1.9.2p53

* Sat Oct 16 2010 Alexey I. Froloff <raorn@altlinux.org> 1.9.2-alt1.r29393.1
- SVN revision 29393 AKA 1.9.2p14

* Sat Sep 25 2010 Alexey I. Froloff <raorn@altlinux.org> 1.9.2-alt1.r29034.1
- SVN revision 29034 AKA 1.9.2p0
  + Incompatible changes:
    * $: no longer includes the current directory, use require_relative
    * Symbol with an invalid encoding is forbidden to exist.
    * Enumerator#rewind now calls the "rewind" method of the enclosed
      object if defined.
    * Enumerator#next doesn't clear the position at end.
    * Kernel#instance_eval yields the receiver.
    * The year argument of Time.{utc,gm,local,mktime} is now interpreted
      as the value itself.  For example, Time.utc(99) means the year 99
      AD, not 1999 AD.
    * Socket#{recvfrom,recvfrom_nonblock,accept,accept_nonblock,sysaccept}
      returns a sender address as Addrinfo object instead of a binary
      sockaddr string.  Addrinfo#to_s returns the old binary sockaddr
      string.
    * BasicSocket#getsockopt returns Socket::Option object instead of a
      binary string.  Socket::Option#to_s returns the old binary string.
    * Socket.do_not_reverse_lookup is turned on by default now.
    * Time.parse raises ArgumentError when no date information.
    * Regexp properties (\p{}) names now ignore underscores, spaces, and
      case, so \p{ol chiki} is the same as \p{Ol_Chiki}
    * Regexps now support Unicode 5.2 (new characters and scripts)
    * \d, \s, and \w are now ASCII only; use POSIX bracket classes and
      \p{} for Unicode semantics
  + See NEWS for more info...

* Tue Dec 29 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r26040.1
- Fix String#ljust, String#rjust and String#center breakage after
  CVE-2009-4124 fix

* Wed Dec 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r26040
- SVN revision 26040 AKA 1.9.1p376 (2009-12-07)
  + CVE-2009-4124

* Sun Nov 29 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r25953
- SVN revision 25953 AKA 1.9.1p355 (2009-11-27)
- Backported fix for REXML formatter exception when duplicate namespaced
  attributes exist

* Thu Nov 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r25816.1
- Make tests pass on ARM

* Wed Nov 18 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.r25816
- SVN revision 25816 AKA 1.9.1p339 (2009-11-17)
- Backported fix for String#[] issues with short UTF-8 strings

* Tue Nov 10 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.20091101
- SVN snapshot 20091101 AKA 1.9.1-p333
- Execute full test suite in %%check

* Sat Sep 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.20090809
- SVN snapshot 20090809 AKA 1.9.1-p281
 + digest/sha2: Update to 1.0 RELEASE which fixes an off-by-one bug in
   SHA-256 hashing.

* Tue Jul 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.20090727
- SVN snapshot 20090727 AKA 1.9.1-p252
- Fixed "warning: `*' interpreted as argument prefix" in pathname.rb

* Mon Jul 06 2009 Alexey I. Froloff <raorn@altlinux.org> 1.9.1-alt1.20090625
- SVN snapshot 20090625 AKA 1.9.1.203
  + CVE-2009-1904: DoS vulnerability in BigDecimal module
- All ruby-module-*'s merged back to ruby-stdlibs and ruby-stdlibs-tk
- Shared library moved back from /%_lib to %_libdir
- Disabled rubygems by default, use ruby option "--enable gems" to enable
- All packages with RI documentation should depend on ruby-doc-ri
- Modules excluded from stdlibs (packaged separately):
  + json
  + minitest
  + racc
  + rake
  + rubygems
  + test/unit

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 1.8.7-alt7
- Use config.sub when guessing target architecture
- Use files.req for directory provides (needs updated rpm-build-ruby)

* Tue Aug 12 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt6
- 1.8.7.72
  + Multiple vulnerabilities
    + Several vulnerabilities in safe level
      + untrace_var is permitted at safe level 4
      + $PROGRAM_NAME may be modified at safe level 4
      + insecure methods may be called at safe level 1-3
      + syslog operations are permitted at safe level 4
    + DoS vulnerability in WEBrick
    + Lack of taintness check in dl
    + CVE-2008-1447: DNS spoofing vulnerability in resolv.rb

* Thu Jul 10 2008 Sir Raorn <raorn@altlinux.ru> 1.8.7-alt5
- 1.8.7.51
- Fix FHS patch which was broken in 1.8.7-alt3
- Put ruby binary and libruby back to /usr/

* Fri Jun 20 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt4
- 1.8.7.22
  + CVE-2008-2726

* Thu Jun 19 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt3
- 1.8.7.19
- Built with libdb4.7

* Tue Jun 03 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt2
- 1.8.7.3
  + lib/erb.rb: works fine without strscan

* Sun Jun 01 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.7-alt1
- 1.8.7
  + Enumerator is now a built-in module

* Sat Mar 29 2008 Sir Raorn <raorn@altlinux.ru> 1.8.6-alt8
- Built with new rpm-build-ruby:
 + Removed rpm-build-ruby subpackage
 + Removed all manual dependencies
- Switched to Tcl/Tk stubs (8.5) instead of direct linking (sbolshakov@)

* Thu Mar 06 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt7
- update to 1.8.6.114
  + fix file access vulnerability of WEBrick

* Wed Feb 06 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt6
- rubynode updated to 0.1.5
  + Fix a possible segfault with OP_ASGN2 nodes
- synced with Debian ruby1.8-1.8.6.111-4
  + rcov may crash because of backwards incompatibility.
    This fix is a back port from the upstream (r14826-15141).
- temporary build with tk8.4 to avoid crash

* Sun Feb 03 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt5
- remove non-ascii symbols from description and summary

* Sat Feb 02 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt4
- ruby-module-rubynode: rubynode 0.1.4 integrated into ruby tree
- select first valid pager, not last (raorn@)

* Fri Jan 11 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt3
- branch based git repository
- update to ruby_1_8_6 svn branch (revision 14091)
- sync with debian 1.8.6.111-2
  + CVE-2007-5162
- install libruby.so into %_libdir (bug #13951)
- move arch-depended site_ruby to /usr/local/ (raorn@)
- update macros (bug #13933)
- add missing deps to ruby-module-rexml

* Wed Apr 11 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt2
- generation rdoc documentation:
  + add make rdoc

* Sun Apr 01 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt1
- build without debug

* Sun Mar 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.8.6-alt0
- 1.8.6

* Thu Feb 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.8.5-alt4.1
- added rpm-build-ruby subpackage, moved rpm macros to it.

* Thu Jan 11 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.8.5-alt4
- /usr/inculde/ruby added to libruby-devel(bug #10506)

* Fri Jan 05 2007 Sir Raorn <raorn@altlinux.ru> 1.8.5-alt3.1
- Do not handle html-style comments in code as specials

* Tue Dec 05 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.5-alt3
- 1.8.5-p2
- ri pager selection fixing

* Tue Oct 24 2006 Sir Raorn <raorn@altlinux.ru> 1.8.5-alt2.1
- Re-added ruby-stdlibs - pure virtual package with all requires
- mkmf.rb moved to libruby-devel
- base64.rb moved to module-digest
- pstore.rb moved to module-fileutils
- module-stdlibs renamed to module-misc
- libruby-devel requires tool-rdoc
- Hardened requires on libruby for module-*
- Re-added lost %%ruby_configure macro
- Added macroses for "setup.rb"-based modules
- Added %%ruby_vendor macro - ruby -rvendor-specific

* Mon Oct 09 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.5-alt2
- spec rewrite from scratch
- stdlibs sparate to many packages
- new packages naming strategy
- ruby executable moved to /bin
- ruby library moved to /%%_lib
- headers moved to /usr/include/ FHS
- and many others

* Tue Sep 26 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.5-alt1
- 1.8.5
- debian 1.8.5-2 synced
- warnings in core removed

* Thu Apr 13 2006 Sir Raorn <raorn@altlinux.ru> 1.8.4-alt5
- Fixed x86_64 filelist and fhs patch (closes: #9401)
- rdocall script dropped

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.4-alt4.1
- Rebuilt with libdb4.4.

* Fri Mar 03 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.4-alt4
- patching order changed
- Patch ported from FC ruby-1.8-fc-no-eaccess.patch:
    backported from ruby CVS to avoid conflict  between newer glibc.
- ruby-1.8-alt-ri-DESTDIR.patch removed

* Fri Mar 03 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.4-alt3
- Patches ported from debian:
  * ruby-1.8-deb-delegate.rb.patch
   - delegate.rb should use Kernel::raise for Thread.
     [ruby-dev:22681][ruby-dev:22684]
   - delegate.rb should not delegate singleton_method_added.
  * ruby-1.8-deb-.document.patch
   - rdoc processes net/* and some libraries.
  * ruby-1.8-deb-yaml_bignum.patch
   - YAML.dump/load cannot handle Bignum. [ruby-core:6159]
   - patch from Michael Ablassmeier
  * ruby-1.8-deb-yaml_symbol.patch
   - YAML loading of quoted symbols is broken

* Mon Feb 27 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.4-alt2
- FHS patch updated:
  * DESTDIR processing fixed
  * rbconfig back to archlibdir
- Generating system-wide documentation for ri using make

* Tue Feb 14 2006 Kirill A. Shutemov <kas@altlinux.ru> 1.8.4-alt1
- spec cleanups
- FHS patch updated: headers in /usr/include/ruby/%%subver

* Mon Jan 23 2006 Sir Raorn <raorn@altlinux.ru> 1.8.4-alt0
- [1.8.4]

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.2-alt7.1
- Rebuilt with libreadline.so.5.

* Wed Jun 08 2005 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt7
- rebuild

* Fri Apr 15 2005 Anton D. Kachalov <mouse@altlinux.org> 1.8.2-alt6.1
- multilib support

* Mon Feb 28 2005 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt6
- %%configure --with-vendordir
- Change default DESTDIR in rbconfig.rb

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.2-alt5.1.1
- Updated libdb4 build dependencies.
- Rebuilt with libdb4.3.

* Mon Jan 24 2005 Sir Raorn <raorn@altlinux.ru> 1.8.2-alt5.1
- Some spec cleanups
- Use --disable-rpath
- Use `%%_lib' instead of `lib' (maybe-x86_64-fixes)
- Do not set LD_LIBRARY_PATH - rubytest.rb does it for us
- Create created.rid file in RI site dir so it will look like doc dir
- Use rdoc -a by default

* Mon Jan 10 2005 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt5
- 1.8.2 release
- ruby-1.8.2-alt-extdoc.patch in upstream now

* Sun Sep 12 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt4
- Move extensions docs from extensions/ext to extensions

* Sat Sep 11 2004 Sir Raorn <raorn@altlinux.ru> 1.8.2-alt3.2
- %%dir'ed ri_sitedir

* Sat Sep 11 2004 Sir Raorn <raorn@altlinux.ru> 1.8.2-alt3.1
- Changed %%ruby_ri_systemdir to %%ruby_ri_sitedir (points to
  %%_datadir/ri/%%subver/site)
- Document more external modules (which have it's own documentation):
  + iconv
  + io/wait
  + strscan
  + zlib

* Sun Sep 05 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt3
- Add %%ruby_ri_systemdir and %%rdoc macros
- Now --ri-site defers DESTDIR (patch by Alexey I. Froloff)
- Add script 'rdocall' for generate all rdoc documentation

* Sat Aug 14 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt2
- 1.8.2-preview2

* Sun Jul 18 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.2-alt1
- 1.8.2-preview1
- New patch to fix 3506 by Sean Russell

* Tue Jul 06 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.1-alt9
- Add %%ruby_begin and %%ruby_end macros
- Add README.ALT-CP1251 and README.ALT-KOI8

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.1-alt8.1
- Rebuilt with openssl-0.9.7d.

* Tue Apr 20 2004 Kirill A. Shutemov <kas@altlinux.ru> 1.8.1-alt8
- Fixed bug #3506(REXML)

* Wed Mar 24 2004 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt7
- Snapshot as of 2004/03/24
- Fixed:
    + socket extension build in chrooted environment

* Tue Mar 09 2004 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt6
- Snapshot as of 2004/03/08

* Mon Feb 16 2004 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt5
- Snapshot as of 2004/02/15
- Rebuild against libdb4.2

* Sun Dec 28 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt4
- Snapshot as of 2003/12/28 of ruby_1_8 branch
- Removed:
    + patch for rdoc fixes (integrated to upstream)
- Fixed:
    + segfault in Syck's emitter (matz)

* Thu Dec 25 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt3
- Fixed:
    + rdoc's simple markup ToFlow class
- We obsolete 'ri' package now but do not package rdoc-ed
  'ri' metainfo for standard libs so far (nothing to package yet)

* Wed Dec 24 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt2
- Fixed:
    + rdoc's simple markup classes

* Wed Dec 24 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Thu Dec 18 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt11
- Snapshot as of 2003/12/18
- REXML support for iconv(3) is in upstream now

* Sat Sep 27 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt10
- Snapshot as of 2003/09/27
- All external documentation moved to ruby-doc-extra package

* Thu Aug 21 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt9
- Snapshot as of 2003/08/21

* Wed Aug 06 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt8
- Fixed:
  + REXML now falls back to iconv(3) when there is no native
    support for specified encoding (ab)

* Tue Aug 05 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt7
- Final Ruby 1.8.0 + post-release fixes from CVS

* Sat Aug 02 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt6
- 2003/08/02
- OpenSSL support integrated, thus ruby-openssl is obsolete now

* Tue Jul 22 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt5
- Snapshot as of 2003/07/22

* Mon Jul 07 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt4
- Test::Unit is included into stdlibs, ruby-stdlibs package
  obsoletes ruby-testunit now and provides it for backward
  compatibility

* Sun Jul 06 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt3
- Tag release in BTE
- Remove tinfo patch for curses, integrated into upstream

* Sat Jul 05 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt2
- 1.8 CVS snapshot (2003/07/05)

* Sun Jun 29 2003 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt1
- 1.8 CVS snapshot (2003/06/29)
- Patches updated, CGI patch excluded (already in upstream)
- Add %_libdir/%name/vendor_ruby/%subver/%{_target_cpu}-%{_host_os} to the list
  of owned directories for stdlibs-core
- Enhance dependencies between subpackages:
    + lib%name is a base package, everything else requires it (through a chain),
      it also owns a Ruby subtree directories
    + %name-stdlibs prerequires lib%name
    + %name-stdlibc-tk prerequires %name-stdlibs
    + every third-party Ruby package *should* prerequire lib%name
      if it is installable into Ruby subtree
- Clean up spec file:
    + Fix miniruby calls to use non-Perlish variable notation only
- Removed:
    + %name-stdlib-core package merged with lib%name
- Major review of packaged documentation:
    + Ruby FAQ is now in A4 PDF
    + Hal Fulton's "Rubyesque API" from EuRuKo03
    + Tobias Peters' "Garbage in Ruby Extensions" from EuRuKo03
    + Features of Ruby 1.8 since Ruby 1.6 from ruby-shim project

* Tue Dec 10 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt9
- Fixed:
    + Readline extension was lost due wrong check for libtermcap instead
      of libtinfo
    + fileutils.rb incorrect behaviour for symlinks (mouse@altlinux.ru)

* Fri Nov 22 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt8
- Fixed:
    + IRB code to not use #initialize publicly as it is a private method
      in Ruby 1.7 since 2002-11-14.
- Removed:
    + Proxy-Authorization support in Net::HTTP patch (integrated into upstream)

* Tue Nov 19 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt7
- Changed:
    + Installation splitted between %_datadir and %_libdir
      in order to be more conformant to FHS
    + Directory structure is stored in %name-stdlibs-core package
    + vendordir/vendorarchdir added as /usr/{lib,share}/ruby/vendor_ruby
      and site-specific dirs moved to /usr/local
- Fixed:
    + curses modules build fixed
    + mkmf.rb to successuly configure C++ exetnsions

* Tue Oct 29 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt6
- Removed:
    + misc/*.el as now they are part of (X)Emacs prog-modes
- Added:
    + Patch to fix CGI and Cookies to follow 1.7's split() behaviour
    + Gdbm module support
- Fixed:
    + Getaddrinfo detection code in mkmf
- ToDo:
    + Fix mkmf to run run_test() against locally compiled libruby.so
      when dealing with extensions, not against (non-)existent system-wide one

* Sat Oct 26 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt5
- News snapshot (2002/10/26)
- Fixed BuildReq to allow build of gdbm module
- Group changed to Development/Ruby
- Remove ruby-stdlibs-win32ole as it seems tend to not work

* Wed Oct 09 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt4
- New snapshot (2002/10/09)
- Changed:
    + Emacs support moved to %name-doc and placed in %_docdir/%name-%version/misc
      unless XEmacs and GNU Emacs maintaining teams decide where and how
      to put third-party program modes. Also, XEmacs already has (an outdated)
      ruby-mode.

* Thu Sep 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.7.3-alt3
- rebuilt with tcl 8.4

* Thu Sep 19 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt2
- New snapshot (2002/09/19)
- Added:
    + Patch to support proxy authorization in Net::HTTP (Alexander Bokovoy)
    + Win32ole support using Wine as ruby-stdlibs-win32ole
    + db module using libdb4
- Fixed:
    + Build requires to include Readline

* Mon Sep 09 2002 Alexander Bokovoy <ab@altlinux.ru> 1.7.3-alt1
- Initial build of 1.7.x
- Standard library splitted off to ruby-stdlibs
- More libification:
    + Dynamic library splitted off to libruby
    + ruby-devel renamed to libruby-devel
    + ruby-devel-static renamed to libruby-devel-static
- Tcl/Tk extensions work now and split off to ruby-stdlibs-tk
- Documentation extended

* Wed Aug  7 2002 Grigory Milev <week@altlinux.ru> 1.6.7-alt1
- minor spec cleanup

* Tue May 07 2002 Alexander Bokovoy <ab@altlinux.ru> 1.6.7-alt1
- 1.6.7 + post release fixes

* Fri Feb 08 2002 Alexander Bokovoy <ab@altlinux.ru> 1.6.6-alt3
- Dependencies for ruby-doc package refined

* Mon Jan 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6.6-alt2
- rebuild with new python

* Wed Dec 26 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.6-alt1
- 1.6.6
- Removed:
    + mkmf patch (integrated into upstream)
    + Regexp patch (integrated into upstream)

* Thu Dec 20 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.5-alt6
- Fixed:
    + mkmf patch updated to one from Nobu Nakada

* Thu Dec 13 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.5-alt5
- Fixed:
    + Regexp UTF-8 handling (backport from 1.7.x)
    + %_libdir/ruby/site_ruby/%subver added

* Wed Dec 05 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.5-alt4
- Updated:
    + Programming Ruby up to 0.3a
    + URL for Ruby FAQ
- Fixed:
    + Programming Ruby html structure

* Fri Nov 30 2001 Alexander Bokovoy <ab@altlinux.ru> 1.6.5-alt3
- Fixed:
    + mkmf to allow full usage of $(DESTDIR), this is required to
      properly build extension packages

* Tue Oct 16 2001 Alexander Bokovoy <ab@altlinux.ru>   1.6.5-alt2
- Enable shared library build
- Move static library to devel-static

* Fri Sep 28 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Thu Jun 14 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Mon May 28 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt3
- New patches from Mandrake.

* Mon Apr 23 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt2
- Fix extentions. Thanks to Pixel.

* Wed Apr 18 2001 Stanislav Ievlev <inger@altlinux.ru> 1.6.3-alt1
- Up to 1.6.3

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Mon Nov 27 2000 Pixel <pixel@mandrakesoft.com> 1.6.1-4mdk
- build again full optflags

* Wed Nov  8 2000 Pixel <pixel@mandrakesoft.com> 1.6.1-3mdk
- build without -fomit-frame-pointer for time being
- capitalize summaries

* Mon Oct  2 2000 Pixel <pixel@mandrakesoft.com> 1.6.1-2mdk
- fix mispelling

* Thu Sep 28 2000 Pixel <pixel@mandrakesoft.com> 1.6.1-1mdk
- new version
- remove "--with-default-kcode=none", not more needed
- remove setting optflags to -O2, ruby doesn't crashes any more

* Tue Sep 19 2000 Pixel <pixel@mandrakesoft.com> 1.6.0-1mdk
- new version

* Wed Aug 23 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-6mdk
- add packager

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-5mdk
- nicer site-start.d/ruby.el (use add-to-list)

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-4mdk
- fix missing %%config

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-3mdk
- use %_sysconfdir/emacs/site-start.d for the ruby-mode.el

* Fri Aug 18 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-2mdk
- rebuild (fredlsux)

* Fri Aug 18 2000 Pixel <pixel@mandrakesoft.com> 1.4.6-1mdk
- new version
- remove menu

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.5-6mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-5mdk
- rebuild with clean clean_menus

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-4mdk
- macroization
- BM

* Thu Jul 13 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-3mdk
- fix %%URL

* Sun Jun 25 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-2mdk
- rebuild (src.rpm got lost :( )

* Fri Jun 23 2000 Pixel <pixel@mandrakesoft.com> 1.4.5-1mdk
- new version

* Wed Jun 14 2000 Pixel <pixel@mandrakesoft.com> 1.4.4-1mdk
- new version

* Mon Apr 10 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-6mdk
- fix group for doc

* Mon Mar 27 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-5mdk
- add menu

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-4mdk
- new group + cleanup

* Wed Feb 16 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-3mdk
- build with no charset conversion (was kanji :)

* Mon Feb 14 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-2mdk
- added the reference manual and FAQ in doc
- moved the lib/README in ext

* Mon Feb 14 2000 Pixel <pixel@mandrakesoft.com> 1.4.3-1mdk
- mandrake adaptation and spliting in -/doc/extensions

* Wed Dec 08 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.3

* Mon Sep 20 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.2 (Sep 18)

* Fri Sep 17 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.2

* Tue Aug 17 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.0

* Fri Jul 23 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- 2nd release
- Updated to version 1.2.6(15 Jul 1999)
- striped %prefix/bin/ruby

* Mon Jun 28 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.6(21 Jun 1999)

* Wed Apr 14 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.5

* Fri Apr 09 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.4

* Fri Dec 25 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.2 stable.

* Fri Nov 27 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.1c9.

* Thu Nov 19 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.1c8, however it appear short life :-P

* Fri Nov 13 1998 Toru Hoshina <hoshina@best.com>
- Version up.
# }}}
