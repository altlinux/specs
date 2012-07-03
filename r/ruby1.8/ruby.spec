# hey Emacs, its -*- rpm-spec -*-
# vim: set ft=spec fdm=marker :

# NOTES:
# * Ruby in ALTLinux build with integrated rubynode module. Due rpm-build-ruby uses this one.
#

# TODO:
# * Requires to emacs autolding mode
#

# Macroses
%define name                  ruby
%define base_name             ruby
%define version               1.8.7
%define release               11
%define package_name          %{name}1.8

%define subver                %(echo %version |cut -d. -f1,2)
%define platform              %(echo %_target_platform | sed -e 's,-%_vendor,,')

%define rubylibdir_base       %_datadir/%base_name
%define rubylibdir            %_datadir/%base_name/%subver

%define archdir_base          %_libdir/%base_name
%define archdir               %archdir_base/%subver/%platform

%define vendordir_base        %_datadir/%base_name/vendor_ruby
%define vendordir             %vendordir_base/%subver

%define vendorarchdir_base    %_libdir/%base_name/vendor_ruby
%define vendorarchdir         %vendorarchdir_base/%subver/%platform

%define ruby_ri_dir_base      %_datadir/ri
%define ruby_ri_dir           %ruby_ri_dir_base/%subver

%define rubyincludedir        %_includedir/%base_name/%subver
%define rubyhdrdir            %_includedir/%base_name/%subver
%define vendorhdrdir          %rubyhdrdir/vendor_ruby

# Place for noarch ruby modules, installed without RPM.
%define sitedir              %_prefix/local/share/%base_name/site_ruby
# Place for architecture dependend ruby modules, installed without RPM.
%define sitedir_arch         %_prefix/local/%_lib/%base_name/site_ruby

%set_verify_elf_method fhs=normal

Name: %package_name
Version: %version
Release: alt%release
Summary: Interpreter of object-oriented scripting language Ruby %subver
License: Dual: GPL and Ruby
Url: http://www.ruby-lang.org/
Group: Development/Ruby
Requires: lib%name = %version-%release
Provides: ruby = %version-%release
Conflicts: ruby > %version-%release
Conflicts: ruby < %version-%release

Source: %name-%version.tar

Patch1: 1.8-add-docs.patch
Patch2: 1.8-install-digest-h-into-rubyincludedir.patch
Patch4: 1.8-903_rdoc_documents.patch
Patch5: 1.8-Do-not-handle-html-style-comments-in-code-as-specials.patch
Patch6: 1.8-ri-pager-selection-fixing.patch
Patch7: 1.8-808_rexml_document_transitive.patch
Patch8: 1.8-803_soap_massmem.patch
Patch11: 1.8-fhs.patch

Patch22: ruby-1.9.2-alt-ri_cache_utility.patch
Patch23: ruby-1.9.2-alt-group_member_3-is-not-handled-by-fakeroot_1.patch

Patch30: 1.8-rubynode-0.1.5.patch
Patch31: 1.8-config-h.patch

Patch40: ruby-1.8.7-alt-rubyhdrdir.patch
Patch41: ruby-1.8.7-alt-logger.patch
Patch42: ruby-1.8.7-alt-fix_depend_file.patch

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildRequires: groff-base libdb4-devel libgdbm-devel libncurses-devel libreadline-devel libssl-devel tk-devel zlib-devel rpm-build-ruby
BuildRequires: gcc-c++

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.
Interpreter of object-oriented scripting language Ruby %subver.

# Base libraries

%package -n lib%name
Summary: Libraries necessary to run the Ruby %subver
Group: System/Libraries
Provides: %archdir
Provides: %rubylibdir
Provides: %vendorarchdir
Provides: %vendordir
Provides: lib%base_name
#In ruby 1.8.6 you have to require 'enumerator' (which is part of stdlib and has been merged into core in 1.8.7+) before using each_slice.
#require 'enumerator' needed in ruby <= 1.8.6 only
Provides: ruby1.8(enumerator)
Requires: %name = %version-%release

%description -n lib%name
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.
This package includes the libruby, necessary to run Ruby %subver.

# Development

%package -n lib%name-devel
Summary: Header files for compiling extension modules for the Ruby %subver
Group: Development/Ruby
Requires: lib%name = %version-%release
Requires: %name-tool-rdoc = %version-%release
Requires: %name-stdlibs = %version-%release
Requires: rpm-build-ruby

Provides: lib%base_name-devel = %version-%release
Conflicts: lib%base_name-devel > %version-%release
Conflicts: lib%base_name-devel < %version-%release

%description -n lib%name-devel
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.
This package contains the header files, necessary to make extension
library for Ruby %subver.

# Static development

%package -n lib%name-devel-static
Summary: Statically linked Ruby %subver library
Group: Development/Ruby
Requires: lib%name-devel = %version-%release

Provides: lib%base_name-devel-static = %version-%release
Conflicts: lib%base_name-devel-static > %version-%release
Conflicts: lib%base_name-devel-static < %version-%release

%description -n lib%name-devel-static
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.
This package includes statically linked Ruby %subver library needed for 
embedding Ruby in other applications.

# Examples

%package -n %name-doc-examples
Summary: This package provides example programs about Ruby %subver
Group: Development/Ruby
Provides: %base_name-doc-examples

%description -n %name-doc-examples
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

# RI documentation

%package -n %name-doc-ri
Summary: This package provides ri documentation for Ruby %subver
Group: Development/Ruby
Requires: %name-tool-ri
Requires: lib%name = %version-%release
Provides: %base_name-doc-ri
Provides: %ruby_ri_dir/site

BuildArch: noarch

%description -n %name-doc-ri
This package provides ri documentation for Ruby %subver

# Interactive ruby

%package -n %name-tool-irb
Summary: Interactive Ruby (for Ruby %subver)
Group: Development/Ruby
Requires: %name = %version-%release
Requires: lib%name = %version-%release
Requires: %name-tool-rdoc = %version-%release
Requires: %name-stdlibs = %version-%release

Provides: %base_name-tool-irb = %version-%release
Conflicts: %base_name-tool-irb > %version-%release
Conflicts: %base_name-tool-irb < %version-%release

BuildArch: noarch

%description -n %name-tool-irb
The irb is acronym for Interactive RuBy. It evaluates Ruby expression from
the terminal.
This package provides the irb which uses Ruby %subver.

# rdoc

%package -n %name-tool-rdoc
Summary: Generate documentation from Ruby source files (for Ruby %subver)
Group: Development/Ruby
Requires: %name = %version-%release
Requires: lib%name = %version-%release 
Requires: %name-stdlibs = %version-%release
Requires: %name-tool-irb = %version-%release

Provides: %base_name-tool-rdoc = %version-%release
Conflicts: %base_name-tool-rdoc > %version-%release
Conflicts: %base_name-tool-rdoc < %version-%release

BuildArch: noarch

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

# ri

%package -n %name-tool-ri
Summary: Ruby Interactive reference (for Ruby %subver)
Group: Development/Ruby
Requires: %name = %version-%release
Requires: lib%name = %version-%release
Requires: %name-stdlibs = %version-%release
Requires: %name-tool-rdoc = %version-%release

Provides: %base_name-tool-ri = %version-%release
Conflicts: %base_name-tool-ri > %version-%release
Conflicts: %base_name-tool-ri < %version-%release

BuildArch: noarch

%description -n %name-tool-ri
ri is a command line tool that displays descriptions of built-in Ruby
methods, classes, and modules. For methods, it shows you the calling
sequence and a description. For classes and modules, it shows a
synopsis along with a list of the methods the class or module
implements.
This package provides ri command and descriptions about Ruby %subver.

# Standard libraries

%package -n %name-stdlibs
Summary: Standard Ruby %subver library
Group: Development/Ruby
Requires: lib%name = %version-%release
Requires: %name = %version-%release
Requires: %name-tool-rdoc = %version-%release

Provides: %base_name-stdlibs = %version-%release
Conflicts: %base_name-stdlibs > %version-%release
Conflicts: %base_name-stdlibs < %version-%release

%description -n %name-stdlibs
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

This package contains standard Ruby %subver runtime library.

# Tk bindings

%package -n %name-stdlibs-tk
Summary: Ruby/Tk bindings
Group: Development/Ruby
Requires: lib%name = %version-%release
Requires: %name-stdlibs = %version-%release
Provides: %base_name-stdlibs-tk

%description -n %name-stdlibs-tk
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in perl). It is simple,
straight-forward, and extensible.

This package contains Ruby/Tk bindings.

%prep
%setup -q -n %name-%version
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch11 -p1
%patch22 -p1
%patch23 -p1

%patch30 -p1
%patch31 -p1

%patch40 -p1
%patch41 -p1
%patch42 -p1

# Display summary directories locations.

true "%%subver             %subver"
true "%%platform           %platform"
true
true "%%rubylibdir_base    %rubylibdir_base"
true "%%rubylibdir         %rubylibdir"
true
true "%%archdir_base       %archdir_base"
true "%%archdir            %archdir"
true
true "%%vendordir_base     %vendordir_base"
true "%%vendordir          %vendordir"
true
true "%%vendorarchdir_base %vendorarchdir_base"
true "%%vendorarchdir      %vendorarchdir"
true
true "%%ruby_ri_dir_base   %ruby_ri_dir_base"
true "%%ruby_ri_dir        %ruby_ri_dir"
true
true "%%vendorhdrdir       %vendorhdrdir"
true "%%rubyincludedir     %rubyincludedir"
true "%%rubyhdrdir         %rubyhdrdir"
true
true "%%sitedir            %sitedir"
true "%%sitedir_arch       %sitedir_arch"


%build
%__autoconf

LDSHARED='gcc -shared' %configure \
--enable-frame-address \
--with-default-kcode=none \
--enable-shared \
--disable-rpath \
--enable-pthread \
--with-sitedir=%_prefix/local/share/%base_name/site_ruby \
--with-sitearchdir=%_prefix/local/%_lib/%base_name/site_ruby \
--with-vendordir=%vendordir_base \
--with-vendorarchdir=%vendorarchdir_base \

%make
%make rdoc


%check
# Hack to pass mkmf checks for socket as it tries to run tests in extensions
# linked against libruby.so which isn't in a LD's path yet
export LD_LIBRARY_PATH="%_builddir/%name-%version-%release"
export PATH="%_builddir/%name-%version-%release:$PATH"
export LANG=en_US.UTF-8
%make test


%install
%makeinstall DESTDIR=%buildroot
%make DESTDIR=%buildroot  do-install-doc

%__mkdir_p %buildroot%_menudir/
%__install -m 644 doc/{erb,irb,rdoc,ri,testrb}.1 %buildroot%_man1dir/
%__install -m 644 doc/irb.menu %buildroot%_menudir/

%__mkdir_p %buildroot%vendordir
%__mkdir_p %buildroot%vendorarchdir

mkdir -p %buildroot%ruby_ri_dir/site

echo "VENDOR_SPECIFIC=true" > %buildroot%vendordir/vendor-specific.rb

mkdir -p %buildroot%_rpmlibdir

cat <<EOF >%buildroot%_rpmlibdir/libruby-files.req.list
# libruby dirlist for %_rpmlibdir/files.req
%archdir lib%name
%rubylibdir lib%name
%vendorarchdir lib%name
%vendordir lib%name
%rubyhdrdir lib%name-devel
%vendorhdrdir lib%name-devel
%ruby_ri_dir/site %name-doc-ri
EOF

# Package ruby-tool-rdoc has an unmet dep:
# Depends: ruby(TestInline.rb)
# Depends: ruby(TestParse.rb)
rm -rf %buildroot%rubylibdir/rdoc/markup/test

#Package ruby-module-rss has an unmet dep:
# Depends: ruby(xmlscan/scanner)
rm -rf %buildroot%rubylibdir/rss/xmlscanner.rb

#Package ruby-module-soap has an unmet dep:
# Depends: ruby(xml/parser)
# Depends: ruby(xmlscan/scanner)
rm -rf %buildroot%rubylibdir/xsd/xmlparser/xmlparser.rb
rm -rf %buildroot%rubylibdir/xsd/xmlparser/xmlscanner.rb

#Package ruby-module-test-unit has an unmet dep:
# Depends: ruby(fox)
# Depends: ruby(gtk)
# Depends: ruby(gtk2)
rm -rf %buildroot%rubylibdir/test/unit/ui/fox
rm -rf %buildroot%rubylibdir/test/unit/ui/gtk
rm -rf %buildroot%rubylibdir/test/unit/ui/gtk2

#Package ruby-module-xmlrpc has an unmet dep:
# Depends: ruby(nqxml/streamingparser)
# Depends: ruby(nqxml/treeparser)
# Depends: ruby(xmlparser)
# Depends: ruby(xmlscan/parser)
# Depends: ruby(xmltreebuilder)
%add_findreq_skiplist %rubylibdir/xmlrpc/create.rb
%add_findreq_skiplist %rubylibdir/xmlrpc/parser.rb


#  RI filetrigger
cat <<EOF >>%buildroot%_rpmlibdir/%base_name-doc-ri.filetrigger
#!/bin/sh

LC_ALL=C grep -qs '^%ruby_ri_dir/site/' || exit 0
exec %_bindir/update-ri-cache %ruby_ri_dir/site
EOF
chmod +x %buildroot%_rpmlibdir/%base_name-doc-ri.filetrigger


# Use compiled ruby in rpm-build-ruby macroses
cat <<EOF >%buildroot/.%base_name.sh
#!/bin/sh

LD_LIBRARY_PATH="%buildroot%_libdir" \
exec \
%buildroot%_bindir/%base_name \
-I "%buildroot%vendordir:%buildroot%vendorarchdir:%buildroot%rubylibdir:%buildroot%archdir" \
"\$@"
EOF
chmod +x %buildroot/.%base_name.sh

%define __ruby %buildroot/.%base_name.sh

# This is a hack but we really don't need to bytecompile
# Python comparison sample in the Ruby manual
unset RPM_PYTHON

%files
%doc ChangeLog* COPYING* LEGAL README* ToDo
%_bindir/%base_name
%_man1dir/%base_name.1*

%files -n lib%name
%_libdir/lib%base_name.so.%subver
%_libdir/lib%base_name.so.%version
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
%config %_rpmlibdir/libruby-files.req.list

%files -n lib%name-devel
%_libdir/lib%base_name.so
%dir /usr/include/ruby
%rubyincludedir/
%rubylibdir/mkmf.rb

%files -n lib%name-devel-static
%_libdir/lib%base_name-static.a

%files -n %name-doc-ri
%_bindir/update-ri-cache
%_rpmlibdir/%base_name-doc-ri.filetrigger
%ruby_ri_dir_base

%files -n %name-tool-irb
%_bindir/irb
%_man1dir/irb.1*
%_menudir/irb.menu
%rubylibdir/irb.rb
%rubylibdir/irb/
%doc doc/irb/

%files -n %name-tool-rdoc
%_bindir/rdoc
%_man1dir/rdoc.1*
%rubylibdir/rdoc/
%doc lib/rdoc/README

%files -n %name-tool-ri
%_bindir/ri
%_man1dir/ri.1*

%files -n %name-stdlibs

# erb
%_bindir/erb
%_bindir/testrb
%_man1dir/erb.1*
%_man1dir/testrb.1*

# Libraries
%archdir
%exclude %archdir/*.rb

# Moldules
%rubylibdir

# Exclude Tk/Tcl files from stdlibs
%exclude %rubylibdir/tk
%exclude %rubylibdir/tkextlib
%exclude %rubylibdir/*-tk.rb
%exclude %rubylibdir/tk*.rb
%exclude %rubylibdir/tk.rb
%exclude %rubylibdir/tcltk.rb
%exclude %archdir/tcltklib.so
%exclude %archdir/tkutil.so

# Exclude devel files from stdlibs
%exclude %rubylibdir/mkmf.rb

# Exclude irb files from stdlibs
%exclude %rubylibdir/irb.rb
%exclude %rubylibdir/irb/

# Exclude rdoc files from stdlibs
%exclude %rubylibdir/rdoc/

# Exclude tk dependency
%exclude %rubylibdir/test/unit/ui/tk/

%files -n %name-stdlibs-tk
%rubylibdir/tk
%rubylibdir/tkextlib
%rubylibdir/*-tk.rb
%rubylibdir/tk*.rb
%rubylibdir/tk.rb
%rubylibdir/tcltk.rb
%archdir/tcltklib.so
%archdir/tkutil.so
%rubylibdir/test/unit/ui/tk/

%changelog
* Thu Oct 20 2011 Timur Aitov <timonbl4@altlinux.org> 1.8.7-alt11
- Fixed build

* Wed May 04 2011 Timur Aitov <timonbl4@altlinux.org> 1.8.7-alt10
- Fixed conflicts in -stdlibs

* Tue May 03 2011 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt9
- fix -stdlibs requires -stdlibs-tk issues

* Mon Apr 25 2011 Timur Aitov <timonbl4@altlinux.org> 1.8.7-alt8
- Fixed post-install unowned files warnings issued by girar
- Added ruby1.8 to depending libruby1.8
- ruby1.8-{doc-ri,tool-irb,tool-rdoc,tool-ri} are made as noarch

* Fri Apr 22 2011 Andriy Stepanov <stanv@altlinux.ru> 1.8.7-alt7
- Adopt Provides/Requires.

* Thu Apr 21 2011 Timur Aitov <timonbl4@altlinux.org> 1.8.7-alt6
- Added conflicts with Ruby 1.9.2

* Tue Apr 19 2011 Timur Aitov <timonbl4@altlinux.org> 1.8.7-alt5
- Fixed logger.rb

* Mon Apr 18 2011 Timur Aitov <timonbl4@altlinux.org> 1.8.7-alt4
- Added 'rubyhdrdir' option to config

* Thu Apr 14 2011 Timur Aitov <timonbl4@altlinux.org> 1.8.7-alt3
- Added provides /usr/share/ri/1.8/site

* Thu Apr 14 2011 Timur Aitov <timonbl4@altlinux.org> 1.8.7-alt2
- Removed dependency ruby1.8(gtk2)
- Added provides ruby1.8(enumerator)

* Fri Apr 01 2011 Andriy Stepanov <stanv@altlinux.ru> 1.8.7-alt1
- Resurrection 1.8.7.
