%define        gemname hoe-travis

Name:          gem-hoe-travis
Version:       1.3.1
Release:       alt1
Summary:       hoe-travis is a Hoe plugin that allows your gem to gain maximum benefit from http://travis-ci.org
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drbrain/hoe-travis
Vcs:           https://github.com/drbrain/hoe-travis.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe) >= 3.0 gem(hoe) < 4
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(hoe) >= 3.0 gem(hoe) < 4
Provides:      gem(hoe-travis) = 1.3.1


%description
hoe-travis is a Hoe plugin that allows your gem to gain maximum benefit from
http://travis-ci.org. The plugin contains a <code>.travis.yml</code> generator
and a pre-defined rake task which runs the tests and ensures your manifest file
is correct.

With hoe-travis it is easy to add additional checks. Custom checks can be easily
verified locally by simply running a rake task instead of committing and pushing
a change, waiting for travis to run your tests, then trying a new commit if you
didn't fix the problem.


%package       -n gem-hoe-travis-doc
Version:       1.3.1
Release:       alt1
Summary:       hoe-travis is a Hoe plugin that allows your gem to gain maximum benefit from http://travis-ci.org documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-travis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-travis) = 1.3.1

%description   -n gem-hoe-travis-doc
hoe-travis is a Hoe plugin that allows your gem to gain maximum benefit from
http://travis-ci.org documentation files.

hoe-travis is a Hoe plugin that allows your gem to gain maximum benefit from
http://travis-ci.org. The plugin contains a <code>.travis.yml</code> generator
and a pre-defined rake task which runs the tests and ensures your manifest file
is correct.

With hoe-travis it is easy to add additional checks. Custom checks can be easily
verified locally by simply running a rake task instead of committing and pushing
a change, waiting for travis to run your tests, then trying a new commit if you
didn't fix the problem.

%description   -n gem-hoe-travis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-travis.


%package       -n gem-hoe-travis-devel
Version:       1.3.1
Release:       alt1
Summary:       hoe-travis is a Hoe plugin that allows your gem to gain maximum benefit from http://travis-ci.org development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-travis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-travis) = 1.3.1
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7

%description   -n gem-hoe-travis-devel
hoe-travis is a Hoe plugin that allows your gem to gain maximum benefit from
http://travis-ci.org development package.

hoe-travis is a Hoe plugin that allows your gem to gain maximum benefit from
http://travis-ci.org. The plugin contains a <code>.travis.yml</code> generator
and a pre-defined rake task which runs the tests and ensures your manifest file
is correct.

With hoe-travis it is easy to add additional checks. Custom checks can be easily
verified locally by simply running a rake task instead of committing and pushing
a change, waiting for travis to run your tests, then trying a new commit if you
didn't fix the problem.

%description   -n gem-hoe-travis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-travis.


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

%files         -n gem-hoe-travis-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-hoe-travis-devel
%doc README.rdoc


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- + packaged gem with Ruby Policy 2.0
