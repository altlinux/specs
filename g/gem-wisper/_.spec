%define        gemname wisper

Name:          gem-wisper
Version:       2.0.1.1
Release:       alt1
Summary:       A micro library providing Ruby objects with Publish-Subscribe capabilities
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/krisleech/wisper
Vcs:           https://github.com/krisleech/wisper.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version wisper:2.0.1.1
Provides:      gem(wisper) = 2.0.1.1


%description
A micro library providing objects with Publish-Subscribe capabilities. Both
synchronous (in-process) and asynchronous (out-of-process) subscriptions are
supported. Check out the Wiki for articles, guides and examples:
https://github.com/krisleech/wisper/wiki

* Decouple core business logic from external concerns in Hexagonal style
architectures
* Use as an alternative to ActiveRecord callbacks and Observers in Rails apps
* Connect objects based on context without permanence
* Publish events synchronously or asynchronously

Note: Wisper was originally extracted from a Rails codebase but is not dependant
on Rails.


%package       -n gem-wisper-doc
Version:       2.0.1.1
Release:       alt1
Summary:       A micro library providing Ruby objects with Publish-Subscribe capabilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wisper
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(wisper) = 2.0.1.1

%description   -n gem-wisper-doc
A micro library providing Ruby objects with Publish-Subscribe capabilities
documentation files.

A micro library providing objects with Publish-Subscribe capabilities. Both
synchronous (in-process) and asynchronous (out-of-process) subscriptions are
supported. Check out the Wiki for articles, guides and examples:
https://github.com/krisleech/wisper/wiki

* Decouple core business logic from external concerns in Hexagonal style
architectures
* Use as an alternative to ActiveRecord callbacks and Observers in Rails apps
* Connect objects based on context without permanence
* Publish events synchronously or asynchronously

Note: Wisper was originally extracted from a Rails codebase but is not dependant
on Rails.

%description   -n gem-wisper-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wisper.


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

%files         -n gem-wisper-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1.1-alt1
- ^ 2.0.1 -> 2.0.1[.1]

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- ^ v2.0.1
- ! spec according to changelog rules

* Fri Aug 09 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
