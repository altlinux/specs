%define        gemname fog-cloudstack

Name:          gem-fog-cloudstack
Version:       0.1.0.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Cloudstack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-cloudstack
Vcs:           https://github.com/fog/fog-cloudstack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 12.3.3 gem(rake) < 14
BuildRequires: gem(rubyzip) >= 1.3.0 gem(rubyzip) < 3
BuildRequires: gem(shindo) >= 0.3 gem(shindo) < 1
BuildRequires: gem(fog-core) >= 2.1 gem(fog-core) < 3
BuildRequires: gem(fog-json) >= 1.1 gem(fog-json) < 2
BuildRequires: gem(fog-xml) >= 0.1 gem(fog-xml) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubyzip >= 2.3.0,rubyzip < 3
%ruby_use_gem_version fog-cloudstack:0.1.0.1
Requires:      gem(fog-core) >= 2.1 gem(fog-core) < 3
Requires:      gem(fog-json) >= 1.1 gem(fog-json) < 2
Requires:      gem(fog-xml) >= 0.1 gem(fog-xml) < 1
Provides:      gem(fog-cloudstack) = 0.1.0.1


%description
Module for the 'fog' gem to support Cloudstack.


%package       -n gem-fog-cloudstack-doc
Version:       0.1.0.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Cloudstack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-cloudstack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-cloudstack) = 0.1.0.1

%description   -n gem-fog-cloudstack-doc
Module for the 'fog' gem to support Cloudstack documentation files.

%description   -n gem-fog-cloudstack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-cloudstack.


%package       -n gem-fog-cloudstack-devel
Version:       0.1.0.1
Release:       alt0.1
Summary:       Module for the 'fog' gem to support Cloudstack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-cloudstack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-cloudstack) = 0.1.0.1
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rake) >= 12.3.3 gem(rake) < 14
Requires:      gem(rubyzip) >= 1.3.0 gem(rubyzip) < 3
Requires:      gem(shindo) >= 0.3 gem(shindo) < 1

%description   -n gem-fog-cloudstack-devel
Module for the 'fog' gem to support Cloudstack development package.

%description   -n gem-fog-cloudstack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-cloudstack.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-fog-cloudstack-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-cloudstack-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0.1-alt0.1
- ^ 0.1.0 -> 0.1.0[.1]

* Mon Jun 24 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
