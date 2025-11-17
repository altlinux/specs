%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-rc4

Name:          gem-ruby-rc4
Version:       0.1.5
Release:       alt1
Summary:       RubyRC4 is a pure Ruby implementation of the RC4 algorithm
License:       MIT
Group:         Development/Ruby
Url:           http://www.caigenichols.com/
Vcs:           https://github.com/caiges/ruby-rc4.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 2.14.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 1.9.3
Requires:      rubygems >= 1.8.11
Provides:      gem(ruby-rc4) = 0.1.5

%description
RubyRC4 is a pure Ruby implementation of the RC4 algorithm.


%if_enabled    doc
%package       -n gem-ruby-rc4-doc
Version:       0.1.5
Release:       alt1
Summary:       RubyRC4 is a pure Ruby implementation of the RC4 algorithm documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-rc4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-rc4) = 0.1.5

%description   -n gem-ruby-rc4-doc
RubyRC4 is a pure Ruby implementation of the RC4 algorithm documentation files.

%description   -n gem-ruby-rc4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-rc4.
%endif


%if_enabled    devel
%package       -n gem-ruby-rc4-devel
Version:       0.1.5
Release:       alt1
Summary:       RubyRC4 is a pure Ruby implementation of the RC4 algorithm development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-rc4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-rc4) = 0.1.5
Requires:      gem(rspec) >= 2.14.1

%description   -n gem-ruby-rc4-devel
RubyRC4 is a pure Ruby implementation of the RC4 algorithm development package.

%description   -n gem-ruby-rc4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-rc4.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-ruby-rc4-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-rc4-devel
%doc LICENSE README.md
%endif


%changelog
* Fri Oct 31 2025 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- ^ 0.1.4 -> 0.1.5

* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt1
- + packaged gem with Ruby Policy 2.0
