%define        gemname rubyntlm

Name:          gem-rubyntlm
Version:       0.6.3
Release:       alt1
Summary:       Ruby/NTLM provides message creator and parser for the NTLM authentication
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/winrb/rubyntlm
Vcs:           https://github.com/winrb/rubyntlm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
# BuildRequires: gem(github_changelog_generator) >= 1.14.3
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 2.11
BuildRequires: gem(simplecov) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency github_changelog_generator >= 1.14.3
Provides:      gem(rubyntlm) = 0.6.3


%description
Ruby/NTLM provides message creator and parser for the NTLM authentication.


%package       -n gem-rubyntlm-doc
Version:       0.6.3
Release:       alt1
Summary:       Ruby/NTLM provides message creator and parser for the NTLM authentication documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubyntlm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubyntlm) = 0.6.3

%description   -n gem-rubyntlm-doc
Ruby/NTLM provides message creator and parser for the NTLM authentication
documentation files.

%description   -n gem-rubyntlm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubyntlm.


%package       -n gem-rubyntlm-devel
Version:       0.6.3
Release:       alt1
Summary:       Ruby/NTLM provides message creator and parser for the NTLM authentication development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubyntlm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubyntlm) = 0.6.3
# Requires:      gem(github_changelog_generator) >= 1.14.3
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 2.11
Requires:      gem(simplecov) >= 0

%description   -n gem-rubyntlm-devel
Ruby/NTLM provides message creator and parser for the NTLM authentication
development package.

%description   -n gem-rubyntlm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubyntlm.


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

%files         -n gem-rubyntlm-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubyntlm-devel
%doc README.md


%changelog
* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- ^ 0.6.2 -> 0.6.3

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
