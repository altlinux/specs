%define        gemname ruby-rc4

Name:          gem-ruby-rc4
Version:       0.1.4
Release:       alt1
Summary:       RubyRC4 is a pure Ruby implementation of the RC4 algorithm
License:       MIT
Group:         Development/Ruby
Url:           http://www.caigenichols.com/
Vcs:           https://github.com/caiges/Ruby-RC4.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names ruby-rc4,rc4
Provides:      gem(ruby-rc4) = 0.1.4


%description
RubyRC4 is a pure Ruby implementation of the RC4 algorithm.


%package       -n gem-ruby-rc4-doc
Version:       0.1.4
Release:       alt1
Summary:       RubyRC4 is a pure Ruby implementation of the RC4 algorithm documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-rc4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-rc4) = 0.1.4

%description   -n gem-ruby-rc4-doc
RubyRC4 is a pure Ruby implementation of the RC4 algorithm documentation files.

%description   -n gem-ruby-rc4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-rc4.


%package       -n gem-ruby-rc4-devel
Version:       0.1.4
Release:       alt1
Summary:       RubyRC4 is a pure Ruby implementation of the RC4 algorithm development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-rc4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-rc4) = 0.1.4
Requires:      gem(rspec) >= 0

%description   -n gem-ruby-rc4-devel
RubyRC4 is a pure Ruby implementation of the RC4 algorithm development package.

%description   -n gem-ruby-rc4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-rc4.


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

%files         -n gem-ruby-rc4-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ruby-rc4-devel
%doc README.md


%changelog
* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt1
- + packaged gem with Ruby Policy 2.0
