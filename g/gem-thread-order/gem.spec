%define        gemname thread_order

Name:          gem-thread-order
Version:       1.1.1
Release:       alt1
Summary:       Test helper for ordering threaded code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/JoshCheek/thread_order
Vcs:           https://github.com/joshcheek/thread_order.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(thread_order) = 1.1.1

%description
Test helper for ordering threaded code (does not depend on gems or stdlib,
tested on 1.8.7 - 2.2, rbx, jruby).


%package       -n gem-thread-order-doc
Version:       1.1.1
Release:       alt1
Summary:       Test helper for ordering threaded code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета thread_order
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(thread_order) = 1.1.1

%description   -n gem-thread-order-doc
Test helper for ordering threaded code documentation files.

Test helper for ordering threaded code (does not depend on gems or stdlib,
tested on 1.8.7 - 2.2, rbx, jruby).

%description   -n gem-thread-order-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета thread_order.


%package       -n gem-thread-order-devel
Version:       1.1.1
Release:       alt1
Summary:       Test helper for ordering threaded code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета thread_order
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(thread_order) = 1.1.1
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-thread-order-devel
Test helper for ordering threaded code development package.

Test helper for ordering threaded code (does not depend on gems or stdlib,
tested on 1.8.7 - 2.2, rbx, jruby).

%description   -n gem-thread-order-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета thread_order.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc Readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-thread-order-doc
%doc Readme.md
%ruby_gemdocdir

%files         -n gem-thread-order-devel
%doc Readme.md


%changelog
* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
