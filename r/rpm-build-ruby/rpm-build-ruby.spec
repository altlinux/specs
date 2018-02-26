Name: rpm-build-ruby
Version: 0.1.1
Release: alt1
Serial: 1

Summary: RPM helper scripts to calculate Ruby dependencies
License: GPL
Group: Development/Other

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

Requires: ruby
Conflicts: rpm-build <= 4.0.4-alt24

AutoReq: yes,noruby

BuildRequires: ruby ruby-module-rubynode

%description
These herlper scripts will look at ruby source files in your package,
and will use this information to generate automatic Requires and Provides
tags for the package.

%prep
%setup -q

%install
mkdir -p %buildroot%_rpmlibdir
for f in ruby.req* ruby.prov*; do
  install -m755 -p "$f" "%buildroot%_rpmlibdir/$f"
done
ln -s ruby.req %buildroot%_rpmlibdir/ruby.prov
install -m644 -p rubyreq.rb %buildroot%_rpmlibdir/rubyreq.rb

mkdir -p %buildroot%_rpmmacrosdir
install -m644 -p ruby.macros %buildroot%_rpmmacrosdir/ruby
install -m644 -p ruby.env %buildroot%_rpmmacrosdir/ruby.env

%check
./test.sh

%files
%_rpmlibdir/ruby.req
%_rpmlibdir/ruby.req.rb
%_rpmlibdir/ruby.req.files
%_rpmlibdir/ruby.prov
%_rpmlibdir/ruby.prov.rb
%_rpmlibdir/ruby.prov.files
%_rpmlibdir/rubyreq.rb
%_rpmmacrosdir/ruby
%_rpmmacrosdir/ruby.env

%changelog
* Fri Apr 08 2011 Timur Aitov <timonbl4@altlinux.org> 1:0.1.1-alt1
- Supported both 1.8.7 and 1.9.2 versions of ruby
- Make difference between 1.8 and 1.9

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1:0.1.0-alt2
- Tests moved to %%check section (bootstrap-friendly)

* Mon Jul 06 2009 Alexey I. Froloff <raorn@altlinux.org> 1:0.1.0-alt1
- Updated for ruby 1.9
- Fixed typo in description (closes: #20624)
- Stop processing on syntax error
- Macros moved to %%_rpmmacrosdir

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.4-alt1
- Parser rewritten without recursion (Kirill A. Shutemov)

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.3-alt1
- Strip '.rb' extension from requires/provides to reduce apt
  cache size
- Process "weak provides" for *.so modules too
- Use files.req mechanism for directory requires (needs recent
  libruby)
- New macros:
  + %%update_setup_rb: update setup.rb script from ruby-tool-setup package
  + %%ruby_test_unit: run tests with testrb script

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.2-alt1
- "class << <var>" block support (kas@)

* Fri Mar 28 2008 Sir Raorn <raorn@altlinux.ru> 1:0.0.1-alt1
- Initial build, based on rpm-build-perl

