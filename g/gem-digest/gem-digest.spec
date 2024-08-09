%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname digest

Name:          gem-digest
Version:       3.1.1
Release:       alt1
Summary:       Provides a framework for message digest libraries
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/digest
Vcs:           https://github.com/ruby/digest.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(digest) = 3.1.1


%description
This module provides a framework for message digest libraries.

You may want to look at OpenSSL::Digest as it supports more algorithms.

A cryptographic hash function is a procedure that takes data and returns a fixed
bit string: the hash value, also known as digest. Hash functions are also called
one-way functions, it is easy to compute a digest from a message, but it is
infeasible to generate a message from a digest.


%if_enabled    doc
%package       -n gem-digest-doc
Version:       3.1.1
Release:       alt1
Summary:       Provides a framework for message digest libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета digest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(digest) = 3.1.1

%description   -n gem-digest-doc
Provides a framework for message digest libraries documentation files.

This module provides a framework for message digest libraries.

You may want to look at OpenSSL::Digest as it supports more algorithms.

A cryptographic hash function is a procedure that takes data and returns a fixed
bit string: the hash value, also known as digest. Hash functions are also called
one-way functions, it is easy to compute a digest from a message, but it is
infeasible to generate a message from a digest.

%description   -n gem-digest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета digest.
%endif


%if_enabled    devel
%package       -n gem-digest-devel
Version:       3.1.1
Release:       alt1
Summary:       Provides a framework for message digest libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета digest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(digest) = 3.1.1
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-digest-devel
Provides a framework for message digest libraries development package.

This module provides a framework for message digest libraries.

You may want to look at OpenSSL::Digest as it supports more algorithms.

A cryptographic hash function is a procedure that takes data and returns a fixed
bit string: the hash value, also known as digest. Hash functions are also called
one-way functions, it is easy to compute a digest from a message, but it is
infeasible to generate a message from a digest.

%description   -n gem-digest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета digest.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-digest-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-digest-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt1
- ^ 3.1.0.1pre -> 3.1.1

* Tue Jul 05 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.0.1-alt1
- ^ 3.1.0 -> 3.1.0.1pre

* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
