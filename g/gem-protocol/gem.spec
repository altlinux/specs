%define        gemname protocol

Name:          gem-protocol
Version:       2.0.0
Release:       alt1
Summary:       Method Protocols for Ruby Classes
License:       GPL-2
Group:         Development/Ruby
Url:           http://flori.github.com/protocol
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gem_hadar) >= 1.9.1 gem(gem_hadar) < 2
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(ruby_parser) >= 3.0 gem(ruby_parser) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.11.0,gem_hadar < 2
Requires:      gem(ruby_parser) >= 3.0 gem(ruby_parser) < 4
Provides:      gem(protocol) = 2.0.0


%description
This library offers an implementation of protocols against which you can check
the conformity of your classes or instances of your classes. They are a bit like
Java Interfaces, but as mixin modules they can also contain already implemented
methods. Additionaly you can define preconditions/postconditions for methods
specified in a protocol.


%package       -n gem-protocol-doc
Version:       2.0.0
Release:       alt1
Summary:       Method Protocols for Ruby Classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(protocol) = 2.0.0

%description   -n gem-protocol-doc
Method Protocols for Ruby Classes documentation files.

This library offers an implementation of protocols against which you can check
the conformity of your classes or instances of your classes. They are a bit like
Java Interfaces, but as mixin modules they can also contain already implemented
methods. Additionaly you can define preconditions/postconditions for methods
specified in a protocol.

%description   -n gem-protocol-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol.


%package       -n gem-protocol-devel
Version:       2.0.0
Release:       alt1
Summary:       Method Protocols for Ruby Classes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(protocol) = 2.0.0
Requires:      gem(gem_hadar) >= 1.9.1 gem(gem_hadar) < 2
Requires:      gem(simplecov) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-protocol-devel
Method Protocols for Ruby Classes development package.

This library offers an implementation of protocols against which you can check
the conformity of your classes or instances of your classes. They are a bit like
Java Interfaces, but as mixin modules they can also contain already implemented
methods. Additionaly you can define preconditions/postconditions for methods
specified in a protocol.

%description   -n gem-protocol-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol.


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

%files         -n gem-protocol-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-protocol-devel
%doc README.rdoc


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
