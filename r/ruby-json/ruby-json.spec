# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname json

Name: ruby-%pkgname
Version: 1.5.1
Release: alt1

Summary: JSON parser and generator
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/json/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Fri Jul 24 2009 (-bi)
BuildRequires: libruby-devel ragel ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
This library can parse JSON texts and generate them from ruby data
structures.

%package utils
Summary: Utilites for %name
Group: Development/Ruby
BuildArch: noarch
Requires: %name = %version-%release

%description utils
Utilites for %name

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

# We don't need no pure json parser.
rm -rf lib/json/pure*

%build
%ruby_config
pushd ext/json/ext/parser
ragel parser.rl -G2 -o parser.c
popd
%ruby_build
for m in generator parser; do
  ln -s "$m/$m.so" "ext/json/ext/$m.so"
done
%ruby_test_unit -Ilib:ext:tests tests/test_*.rb
for m in generator parser; do
  rm -f "ext/json/ext/$m.so"
done

%install
%ruby_install
%rdoc lib/

for f in %buildroot%_bindir/*; do
  mv "$f" "${f%%.rb}"
done

%files
%doc README
%ruby_sitelibdir/*
%ruby_sitearchdir/*
%exclude %ruby_sitelibdir/json/editor.rb

%files utils
%_bindir/*
%ruby_sitelibdir/json/editor.rb

%files doc
%ruby_ri_sitedir/JSON*

%changelog
* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.5.1-alt1
- [1.5.1]

* Sat Sep 25 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.9-alt1
- [1.1.9]

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.7-alt1
- Built for Sisyphus

