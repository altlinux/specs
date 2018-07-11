%define  pkgname bundler
%def_disable man

Name:    ruby-%pkgname
Version: 2.0.1
Release: alt1

Summary: Manage your Ruby application's gem dependencies
License: MIT
Group:   Development/Ruby
Url:     https://bundler.io/
# VCS:   https://github.com/bundler/bundler.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

Requires: bundle = %version-%release
BuildRequires(pre): rpm-build-ruby
#BuildRequires: gem(rake) gem(rdiscount) gem(ronn) gem(rspec) gem(rubocop) gem(mustache) gem(automatiek)
%if_enabled man
BuildRequires: ronn groff-base
%endif

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

%description doc -l ru_RU.UTF-8
Документация для %{name}.


%package -n bundle
Summary: Bundle is the executable file for bundler.
Group: Development/Ruby

BuildArch: noarch

Requires: gem(bundler) = %version
Conflicts: golang-tools


%description -n bundle
Bundle is the executable file for bundler.

%description -n bundle -l ru_RU.UTF-8
Исполняемый файл для утилиты bundler.

%prep
%setup -n %pkgname-%version
%update_setup_rb
rm -f bin/{rake,rspec,rubocop,bundle,bundle1,bundle2,with_rubygems}

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
install -p -m 755 exe/{bundle,bundler} %buildroot/%_bindir
mkdir -p %buildroot%rubygem_gemdir/%pkgname-%version/lib/
mv %buildroot%ruby_sitelibdir/* %buildroot%rubygem_gemdir/%pkgname-%version/lib/

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
#%rake spec:deps
#%rake_spec

%files
%rubygem_gemdir/*
%rubygem_specdir/*

%files doc
%doc README*
%ruby_ri_sitedir/*

%files -n bundle
%_bindir/*
%if_enabled man
%_man1dir/*
%_man5dir/*
%endif

%changelog
* Wed Jan 9 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- Bump to 2.0.1.
- Place library files into gem folder.

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
