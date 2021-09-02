%define        gemname atomic

Name:          gem-atomic
Version:       1.1.101
Release:       alt1
Summary:       An atomic reference implementation for JRuby, Rubinius, and MRI
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/ruby-concurrency/atomic
Vcs:           https://github.com/ruby-concurrency/atomic.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(atomic) = 1.1.101


%description
An atomic reference implementation for JRuby, Rubinius, and MRI.


%package       -n gem-atomic-doc
Version:       1.1.101
Release:       alt1
Summary:       An atomic reference implementation for JRuby, Rubinius, and MRI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета atomic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(atomic) = 1.1.101

%description   -n gem-atomic-doc
An atomic reference implementation for JRuby, Rubinius, and MRI documentation
files.

%description   -n gem-atomic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета atomic.


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
%ruby_gemextdir

%files         -n gem-atomic-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.101-alt1
- + packaged gem with Ruby Policy 2.0
