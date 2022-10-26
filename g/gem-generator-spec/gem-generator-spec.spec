%define        gemname generator_spec

Name:          gem-generator-spec
Version:       0.9.4
Release:       alt1
Summary:       Test Rails generators with RSpec
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/stevehodgkiss/generator_spec
Vcs:           https://github.com/stevehodgkiss/generator_spec.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(activesupport) >= 3.0.0
BuildRequires: gem(railties) >= 3.0.0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names generator_spec,generator-spec
Requires:      gem(activesupport) >= 3.0.0
Requires:      gem(railties) >= 3.0.0
Provides:      gem(generator_spec) = 0.9.4


%description
Test Rails generators with RSpec.


%package       -n gem-generator-spec-doc
Version:       0.9.4
Release:       alt1
Summary:       Test Rails generators with RSpec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета generator_spec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(generator_spec) = 0.9.4

%description   -n gem-generator-spec-doc
Test Rails generators with RSpec documentation files.

%description   -n gem-generator-spec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета generator_spec.


%package       -n gem-generator-spec-devel
Version:       0.9.4
Release:       alt1
Summary:       Test Rails generators with RSpec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета generator_spec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(generator_spec) = 0.9.4
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-generator-spec-devel
Test Rails generators with RSpec development package.

%description   -n gem-generator-spec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета generator_spec.


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

%files         -n gem-generator-spec-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-generator-spec-devel
%doc README.md


%changelog
* Mon Oct 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.4-alt1
- + packaged gem with Ruby Policy 2.0
