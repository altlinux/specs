%define  pkgname bundler
%def_disable man

Name:    ruby-%pkgname
Version: 1.17.1
Release: alt1

Summary: Manage your Ruby application's gem dependencies
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/bundler/bundler

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
%if_enabled man
BuildRequires: ronn groff-base
%endif

Conflicts: golang-tools

%add_findreq_skiplist *.tt

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
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

# Install exe files
cp -a exe %buildroot%ruby_sitelibdir/%pkgname

# Replace wrapper /usr/bin/bundle by symlink to real executable
rm -f %buildroot%_bindir/bundle
ln -svr %buildroot%ruby_sitelibdir/%pkgname/exe/bundle %buildroot%_bindir/bundle

# Remove non-working executables
rm -f %buildroot%_bindir/{rake,rspec,rubocop,bundle1,bundle2}

# Generate documentation
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%if_enabled man
# Generate man page
ronn --roff %buildroot%_mandir/*.ronn
mkdir -p %buildroot%_man1dir
mv %buildroot%_mandir/*.1 %buildroot%_man1dir
mkdir -p %buildroot%_man5dir
mv %buildroot%_mandir/*.5 %buildroot%_man5dir
%endif
rm -rf %buildroot%_mandir/*.ronn

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/*
%ruby_sitelibdir/*
%rubygem_specdir/*
%if_enabled man
%_man1dir/*
%_man5dir/*
%endif

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Oct 30 2018 Pavel Skrylev <majioa@altlinux.org> 1.17.1-alt1
- Bump to 1.17.1.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.6-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.5-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.4-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt3.2
- Rebuild with new Ruby autorequirements.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt3.1
- Disable all ruby(*) autoreqs for bootstrap.
- Disable man page generation for bootstrap.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt3
- Fix gemspec name.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt2
- Clarify ignored modules.
- Use common way to package as gem.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt1
- New version.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.1-alt1
- Initial build for Sisyphus
