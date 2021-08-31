%define        gemname hoe-gemspec2

Name:          gem-hoe-gemspec2
Version:       1.2.0
Release:       alt1
Summary:       Adds support for generation of gemspec files to Hoe
License:       MIT
Group:         Development/Ruby
Url:           http://rubygems.org/gems/hoe-gemspec2
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe) >= 0
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-seattlerb) >= 1.2
BuildRequires: gem(hoe-git) >= 1.3
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Requires:      gem(hoe) >= 0
Provides:      gem(hoe-gemspec2) = 1.2.0


%description
Adds support for generation of gemspec files to Hoe. By default, excludes the
signing key and certificate chain. Use <tt>rake gemspec:full</tt> to include the
signing key and certificate chain.


%package       -n gem-hoe-gemspec2-doc
Version:       1.2.0
Release:       alt1
Summary:       Adds support for generation of gemspec files to Hoe documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-gemspec2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-gemspec2) = 1.2.0

%description   -n gem-hoe-gemspec2-doc
Adds support for generation of gemspec files to Hoe documentation files.

Adds support for generation of gemspec files to Hoe. By default, excludes the
signing key and certificate chain. Use <tt>rake gemspec:full</tt> to include the
signing key and certificate chain.

%description   -n gem-hoe-gemspec2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-gemspec2.


%package       -n gem-hoe-gemspec2-devel
Version:       1.2.0
Release:       alt1
Summary:       Adds support for generation of gemspec files to Hoe development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-gemspec2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-gemspec2) = 1.2.0
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-seattlerb) >= 1.2
Requires:      gem(hoe-git) >= 1.3
Requires:      gem(hoe-gemspec2) >= 0
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7

%description   -n gem-hoe-gemspec2-devel
Adds support for generation of gemspec files to Hoe development package.

Adds support for generation of gemspec files to Hoe. By default, excludes the
signing key and certificate chain. Use <tt>rake gemspec:full</tt> to include the
signing key and certificate chain.

%description   -n gem-hoe-gemspec2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-gemspec2.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-hoe-gemspec2-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-hoe-gemspec2-devel
%doc README.rdoc


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
