%define        pkgname safemode

Name:          gem-%pkgname
Version:       1.3.6
Release:       alt1
Summary:       A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/svenfuchs/safemode
Vcs:           https://github.com/svenfuchs/safemode.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby2ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

Provides Rails ActionView template handlers for ERB and Haml.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir


%changelog
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.6-alt1
- ^ 1.3.5 -> 1.3.6
- ! spec tags

* Sat Mar 23 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.5-alt1
- Initial build for Sisyphus
