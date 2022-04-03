%define        gemname digest

Name:          gem-digest
Version:       3.1.0
Release:       alt1
Summary:       Provides a framework for message digest libraries
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/digest
Vcs:           https://github.com/ruby/digest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(digest) = 3.1.0


%description
This module provides a framework for message digest libraries.

You may want to look at OpenSSL::Digest as it supports more algorithms.

A cryptographic hash function is a procedure that takes data and returns a fixed
bit string: the hash value, also known as digest. Hash functions are also called
one-way functions, it is easy to compute a digest from a message, but it is
infeasible to generate a message from a digest.


%package       -n gem-digest-doc
Version:       3.1.0
Release:       alt1
Summary:       Provides a framework for message digest libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета digest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(digest) = 3.1.0

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


%package       -n gem-digest-devel
Version:       3.1.0
Release:       alt1
Summary:       Provides a framework for message digest libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета digest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(digest) = 3.1.0

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

%files         -n gem-digest-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-digest-devel
%doc README.md
%ruby_includedir/*


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
