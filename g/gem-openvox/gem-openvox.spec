%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname openvox

Name:          gem-openvox
Version:       8.25.0
Release:       alt1
Summary:       OpenVox, a community implementation of Puppet -- an automated configuration management tool
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/OpenVoxProject/openvox
Vcs:           https://github.com/openvoxproject/openvox.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0.1
BuildRequires: gem(benchmark) >= 0.2
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(deep_merge) >= 1.0
BuildRequires: gem(fast_gettext) >= 2.1
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(getoptlong) >= 0.2.0
BuildRequires: gem(json-schema) >= 2
BuildRequires: gem(locale) >= 2.1
BuildRequires: gem(openfact) >= 5.0
BuildRequires: gem(ostruct) >= 0.5.5
BuildRequires: gem(pry) >= 0
BuildRequires: gem(puppet-resource_api) >= 2.0
BuildRequires: gem(racc) >= 1.5
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(rspec-its) >= 1.1
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-i18n) >= 3.0
BuildRequires: gem(rubocop-performance) >= 1.0
BuildRequires: gem(rubocop-rake) >= 0.6
BuildRequires: gem(rubocop-rspec) >= 3.0
BuildRequires: gem(ruby-prof) >= 0.16.0
BuildRequires: gem(scanf) >= 1.0
BuildRequires: gem(semantic_puppet) >= 1.0
BuildRequires: gem(vcr) >= 6.1
BuildRequires: gem(webmock) >= 3.0
BuildRequires: gem(webrick) >= 1.7
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(base64) >= 0.4
BuildConflicts: gem(benchmark) >= 0.6
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(deep_merge) >= 2
BuildConflicts: gem(fast_gettext) >= 5
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(getoptlong) >= 0.3
BuildConflicts: gem(json-schema) >= 6
BuildConflicts: gem(locale) >= 3
BuildConflicts: gem(openfact) >= 6
BuildConflicts: gem(ostruct) >= 0.7
BuildConflicts: gem(puppet-resource_api) >= 3
BuildConflicts: gem(racc) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-its) >= 2
BuildConflicts: gem(rspec-mocks) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-i18n) >= 4
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(scanf) >= 2
BuildConflicts: gem(semantic_puppet) >= 2
BuildConflicts: gem(vcr) >= 7
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(webrick) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec-expectations >= 3.10.1,rspec-expectations < 4
%ruby_use_gem_dependency rspec-mocks >= 3.10.2,rspec-mocks < 4
%ruby_use_gem_dependency ffi >= 1.17.0,ffi < 2
Requires:      ruby >= 3.1.0
Requires:      rubygems > 1.3.1
Requires:      gem(base64) >= 0.1
Requires:      gem(benchmark) >= 0.2
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(deep_merge) >= 1.0
Requires:      gem(fast_gettext) >= 2.1
Requires:      gem(getoptlong) >= 0.2.0
Requires:      gem(locale) >= 2.1
Requires:      gem(openfact) >= 5.0
Requires:      gem(ostruct) >= 0.5.5
Requires:      gem(puppet-resource_api) >= 2.0
Requires:      gem(racc) >= 1.5
Requires:      gem(scanf) >= 1.0
Requires:      gem(semantic_puppet) >= 1.0
Conflicts:     gem(base64) >= 0.4
Conflicts:     gem(benchmark) >= 0.6
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(deep_merge) >= 2
Conflicts:     gem(fast_gettext) >= 5
Conflicts:     gem(getoptlong) >= 0.3
Conflicts:     gem(locale) >= 3
Conflicts:     gem(openfact) >= 6
Conflicts:     gem(ostruct) >= 0.7
Conflicts:     gem(puppet-resource_api) >= 3
Conflicts:     gem(racc) >= 2
Conflicts:     gem(scanf) >= 2
Conflicts:     gem(semantic_puppet) >= 2
Provides:      gem(openvox) = 8.25.0

%description
OpenVox is a community implementation of Puppet, an automated administrative
engine for your Linux, Unix, and Windows systems, performs administrative tasks
(such as adding users, installing packages, and updating server configurations)
based on a centralized specification.


%package       -n openvox
Version:       8.25.0
Release:       alt1
Summary:       OpenVox, a community implementation of Puppet -- an automated configuration management tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета openvox
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(openvox) = 8.25.0
Requires:      gem(openfact) >= 5.0
Requires:      gem(puppet-resource_api) >= 2.0
Requires:      gem(semantic_puppet) >= 1.0
Conflicts:     puppet
Conflicts:     gem(openfact) >= 6
Conflicts:     gem(puppet-resource_api) >= 3
Conflicts:     gem(semantic_puppet) >= 2

%description   -n openvox
OpenVox, a community implementation of Puppet -- an automated configuration
management tool executable(s).

OpenVox is a community implementation of Puppet, an automated administrative
engine for your Linux, Unix, and Windows systems, performs administrative tasks
(such as adding users, installing packages, and updating server configurations)
based on a centralized specification.

%description   -n openvox -l ru_RU.UTF-8
Исполнямка для самоцвета openvox.


%if_enabled    doc
%package       -n gem-openvox-doc
Version:       8.25.0
Release:       alt1
Summary:       OpenVox, a community implementation of Puppet -- an automated configuration management tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета openvox
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(openvox) = 8.25.0

%description   -n gem-openvox-doc
OpenVox, a community implementation of Puppet -- an automated configuration
management tool documentation files.

OpenVox is a community implementation of Puppet, an automated administrative
engine for your Linux, Unix, and Windows systems, performs administrative tasks
(such as adding users, installing packages, and updating server configurations)
based on a centralized specification.

%description   -n gem-openvox-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета openvox.
%endif


%if_enabled    devel
%package       -n gem-openvox-devel
Version:       8.25.0
Release:       alt1
Summary:       OpenVox, a community implementation of Puppet -- an automated configuration management tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета openvox
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(openvox) = 8.25.0
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(json-schema) >= 2
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.1
Requires:      gem(rspec-its) >= 1.1
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-i18n) >= 3.0
Requires:      gem(rubocop-performance) >= 1.0
Requires:      gem(rubocop-rake) >= 0.6
Requires:      gem(rubocop-rspec) >= 3.0
Requires:      gem(ruby-prof) >= 0.16.0
Requires:      gem(vcr) >= 6.1
Requires:      gem(webmock) >= 3.0
Requires:      gem(webrick) >= 1.7
Requires:      gem(yard) >= 0
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(json-schema) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-its) >= 2
Conflicts:     gem(rspec-mocks) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-i18n) >= 4
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(vcr) >= 7
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(webrick) >= 2

%description   -n gem-openvox-devel
OpenVox, a community implementation of Puppet -- an automated configuration
management tool development package.

OpenVox is a community implementation of Puppet, an automated administrative
engine for your Linux, Unix, and Windows systems, performs administrative tasks
(such as adding users, installing packages, and updating server configurations)
based on a centralized specification.

%description   -n gem-openvox-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета openvox.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n openvox
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%_bindir/puppet
%_man5dir/puppet*
%_man8dir/puppet*

%if_enabled    doc
%files         -n gem-openvox-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-openvox-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 8.25.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
