%define  pkgname bundler

Name:    ruby-%pkgname
Version: 1.16.1
Release: alt1

Summary: Manage your Ruby application's gem dependencies
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/bundler/bundler

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Patch1:  alt-gemspec.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ronn groff-base

Conflicts: golang-tools

%add_findreq_skiplist *.tt
%filter_from_requires \,^ruby(rubygems/\(builder\|format\))$,d

%description
Bundler makes sure Ruby applications run the same code on every machine.
It does this by managing the gems that the application depends on. Given
a list of gems, it can automatically download and install those gems, as
well as any other gems needed by the gems that are listed. Before
installing gems, it checks the versions of every gem to make sure that
they are compatible, and can all be loaded at the same time. After the
gems have been installed, Bundler can help you update some or all of
them when new versions become available. Finally, it records the exact
versions that have been installed, so that others can install the exact
same gems.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch1 -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

# Install gemspec
export rbVersion=`ruby -e "puts RbConfig::CONFIG[\"ruby_version\"]"`
install -Dm 0644 %pkgname.gemspec %buildroot%ruby_libdir/gems/$rbVersion/specifications/%pkgname.gemspec

# Install exe files
cp -a exe %buildroot%ruby_sitelibdir/%pkgname

# Replace wrapper /usr/bin/bundle by symlink to real executable
rm -f %buildroot%_bindir/bundle
ln -svr %buildroot%ruby_sitelibdir/%pkgname/exe/bundle %buildroot%_bindir/bundle

# Remove non-working executables
rm -f %buildroot%_bindir/{rake,rspec,rubocop,bundle1,bundle2}

%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

# Generate man page
ronn --roff %buildroot%_mandir/*.ronn
mkdir -p %buildroot%_man1dir
mv %buildroot%_mandir/*.1 %buildroot%_man1dir
mkdir -p %buildroot%_man5dir
mv %buildroot%_mandir/*.5 %buildroot%_man5dir
rm -rf %buildroot%_mandir/*.ronn

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/*
%ruby_sitelibdir/*
%ruby_libdir/gems/*/specifications/%pkgname.gemspec
%_man1dir/*
%_man5dir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.1-alt1
- Initial build for Sisyphus
