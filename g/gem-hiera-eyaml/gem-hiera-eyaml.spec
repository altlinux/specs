%define        gemname hiera-eyaml

Name:          gem-hiera-eyaml
Version:       3.3.0
Release:       alt1
Summary:       A backend for Hiera that provides per-value asymmetric encryption of sensitive data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/voxpupuli/hiera-eyaml
Vcs:           https://github.com/voxpupuli/hiera-eyaml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(aruba) >= 0.6.2
BuildRequires: gem(cucumber) >= 1.1
BuildRequires: gem(rspec-expectations) >= 3.1.0
BuildRequires: gem(hiera-eyaml-plaintext) >= 0
BuildRequires: gem(github_changelog_generator) >= 0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov-console) >= 0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(optimist) >= 0
BuildRequires: gem(highline) >= 0
BuildConflicts: gem(aruba) >= 0.7
BuildConflicts: gem(cucumber) >= 2
BuildConflicts: gem(rspec-expectations) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec-expectations >= 3.10.1,rspec-expectations < 4
Requires:      gem(optimist) >= 0
Requires:      gem(highline) >= 0
Obsoletes:     ruby-hiera-eyaml
Provides:      ruby-hiera-eyaml
Provides:      gem(hiera-eyaml) = 3.3.0


%description
hiera-eyaml is a backend for Hiera that provides per-value encryption of
sensitive data within yaml files to be used by Puppet.


%package       -n eyaml
Version:       3.3.0
Release:       alt1
Summary:       A backend for Hiera that provides per-value asymmetric encryption of sensitive data executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hiera-eyaml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hiera-eyaml) = 3.3.0

%description   -n eyaml
A backend for Hiera that provides per-value asymmetric encryption of sensitive
data executable(s).

hiera-eyaml is a backend for Hiera that provides per-value encryption of
sensitive data within yaml files to be used by Puppet.

%description   -n eyaml -l ru_RU.UTF-8
Исполнямка для самоцвета hiera-eyaml.


%package       -n gem-hiera-eyaml-doc
Version:       3.3.0
Release:       alt1
Summary:       A backend for Hiera that provides per-value asymmetric encryption of sensitive data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hiera-eyaml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hiera-eyaml) = 3.3.0

%description   -n gem-hiera-eyaml-doc
A backend for Hiera that provides per-value asymmetric encryption of sensitive
data documentation files.

hiera-eyaml is a backend for Hiera that provides per-value encryption of
sensitive data within yaml files to be used by Puppet.

%description   -n gem-hiera-eyaml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hiera-eyaml.


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

%files         -n eyaml
%doc README.md
%_bindir/eyaml

%files         -n gem-hiera-eyaml-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- ^ 3.2.0 -> 3.3.0 (no devel)

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- updated (^) 3.0.0 -> 3.2.0
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- fixed (!) spec according to changelog rules

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- updated (^) 2.1.0 -> 3.0.0
- fixed (!) spec

* Wed Apr 10 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.0-alt2
- Use new ruby packaging policy
- Make appropriate require to highline

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build in Sisyphus
