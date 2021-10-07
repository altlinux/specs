%define        gemname andand

Name:          gem-andand
Version:       1.3.3.1
Release:       alt1
Summary:       andand is a method that provides guarded method invocation
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/raganwald/andand/
Vcs:           https://github.com/raganwald/andand.git
Packager:      Andrey Cherepanov <cas@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit
BuildRequires: ruby-tool-rdoc

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version andand:1.3.3.1
Obsoletes:     ruby-andand < %EVR
Provides:      ruby-andand = %EVR
Provides:      gem(andand) = 1.3.3.1


%description
andand is a method that provides guarded method invocation, analagous to the &&
operator in Ruby, and especially &&=.


%package       -n gem-andand-doc
Version:       1.3.3.1
Release:       alt1
Summary:       andand is a method that provides guarded method invocation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета andand
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(andand) = 1.3.3.1

%description   -n gem-andand-doc
andand is a method that provides guarded method invocation, analagous to the &&
operator in Ruby, and especially &&= documentation files.

%description   -n gem-andand-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета andand.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.textile
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-andand-doc
%doc README.textile
%ruby_gemdocdir


%changelog
* Fri Sep 10 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.3.1-alt1
- ^ 1.3.1 -> 1.3.3.1

* Mon Apr 21 2014 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
