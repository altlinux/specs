%define        gemname puppet-strings

Name:          gem-puppet-strings
Version:       2.8.0
Release:       alt1
Summary:       The next generation Puppet documentation extraction and presentation tool
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/puppet-strings
Vcs:           https://github.com/puppetlabs/puppet-strings.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(yard) >= 0.9.5 gem(yard) < 0.10
BuildRequires: gem(rgen) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(yard) >= 0.9.5 gem(yard) < 0.10
Requires:      gem(rgen) >= 0
Provides:      gem(puppet-strings) = 2.8.0


%description
Puppet Strings generates documentation for Puppet code and extensions written in
Puppet and Ruby. Strings processes code and YARD-style code comments to create
documentation in HTML, Markdown, or JSON formats.


%package       -n gem-puppet-strings-doc
Version:       2.8.0
Release:       alt1
Summary:       The next generation Puppet documentation extraction and presentation tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet-strings
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppet-strings) = 2.8.0

%description   -n gem-puppet-strings-doc
The next generation Puppet documentation extraction and presentation tool
documentation files.

Puppet Strings generates documentation for Puppet code and extensions written in
Puppet and Ruby. Strings processes code and YARD-style code comments to create
documentation in HTML, Markdown, or JSON formats.

%description   -n gem-puppet-strings-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppet-strings.


%package       -n gem-puppet-strings-devel
Version:       2.8.0
Release:       alt1
Summary:       The next generation Puppet documentation extraction and presentation tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppet-strings
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppet-strings) = 2.8.0

%description   -n gem-puppet-strings-devel
The next generation Puppet documentation extraction and presentation tool
development package.

Puppet Strings generates documentation for Puppet code and extensions written in
Puppet and Ruby. Strings processes code and YARD-style code comments to create
documentation in HTML, Markdown, or JSON formats.

%description   -n gem-puppet-strings-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppet-strings.


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

%files         -n gem-puppet-strings-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-puppet-strings-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.8.0-alt1
- ^ 2.2.0 -> 2.8.0

* Thu Jun 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
