%define        gemname mspec

Name:          gem-mspec
Version:       1.8.0
Release:       alt1
Summary:       MSpec is a specialized framework for RubySpec
License:       Ruby
Group:         Development/Ruby
Url:           http://rubyspec.org
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 2.8 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(mspec) = 1.8.0


%description
RSpec-like test runner for the Ruby Spec Suite.

MSpec is a specialized framework that is syntax-compatible with RSpec for basic
things like describe, it blocks and before, after actions.  MSpec contains
additional features that assist in writing the RubySpecs used by multiple Ruby
implementations. Also, MSpec attempts to use the simplest Ruby language
features so that beginning Ruby implementations can run it.


%package       -n mkspec
Version:       1.8.0
Release:       alt1
Summary:       MMSpec is a specialized framework for RubySpec executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mspec
Group:         Other
BuildArch:     noarch

Requires:      gem(mspec) = 1.8.0

%description   -n mkspec
MMSpec is a specialized framework for RubySpec executable(s).

RSpec-like test runner for the Ruby Spec Suite.

MSpec is a specialized framework that is syntax-compatible with RSpec for basic
things like describe, it blocks and before, after actions.  MSpec contains
additional features that assist in writing the RubySpecs used by multiple Ruby
implementations. Also, MSpec attempts to use the simplest Ruby language
features so that beginning Ruby implementations can run it.

%description   -n mkspec -l ru_RU.UTF-8
Исполнямка для самоцвета mspec.


%package       -n gem-mspec-doc
Version:       1.8.0
Release:       alt1
Summary:       MMSpec is a specialized framework for RubySpec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mspec) = 1.8.0

%description   -n gem-mspec-doc
MMSpec is a specialized framework for RubySpec documentation files.

RSpec-like test runner for the Ruby Spec Suite.

MSpec is a specialized framework that is syntax-compatible with RSpec for basic
things like describe, it blocks and before, after actions.  MSpec contains
additional features that assist in writing the RubySpecs used by multiple Ruby
implementations. Also, MSpec attempts to use the simplest Ruby language
features so that beginning Ruby implementations can run it.

%description   -n gem-mspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mspec.


%package       -n gem-mspec-devel
Version:       1.8.0
Release:       alt1
Summary:       MMSpec is a specialized framework for RubySpec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mspec) = 1.8.0
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rspec) >= 2.8 gem(rspec) < 4

%description   -n gem-mspec-devel
MMSpec is a specialized framework for RubySpec development package.

RSpec-like test runner for the Ruby Spec Suite.

MSpec is a specialized framework that is syntax-compatible with RSpec for basic
things like describe, it blocks and before, after actions.  MSpec contains
additional features that assist in writing the RubySpecs used by multiple Ruby
implementations. Also, MSpec attempts to use the simplest Ruby language
features so that beginning Ruby implementations can run it.

%description   -n gem-mspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mspec.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n mkspec
%doc README
%_bindir/mkspec
%_bindir/mspec
%_bindir/mspec-ci
%_bindir/mspec-run
%_bindir/mspec-tag

%files         -n gem-mspec-doc
%doc README
%ruby_gemdocdir

%files         -n gem-mspec-devel
%doc README


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- + packaged gem with Ruby Policy 2.0
