%define        pkgname mixlib-config

Name: 	       gem-%pkgname
Version:       3.0.6
Release:       alt1
Summary:       A simple class based Config mechanism, similar to the one found in Chef
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-config
Vcs:           https://github.com/chef/mixlib-config.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Mixlib::Config provides a class-based configuration object, as used in Chef.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jul 10 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.6-alt1
- > Ruby Policy 2.0
- ^ 2.2.14 -> 3.0.6
- ! spec tags

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.14-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.2
- Rebuild for new Ruby autorequirements.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux
