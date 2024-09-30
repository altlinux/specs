%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-gemspec2

Name:          gem-hoe-gemspec2
Version:       1.3.0
Release:       alt1
Summary:       Adds support for generation of gemspec files to Hoe
License:       MIT
Group:         Development/Ruby
Url:           http://rubygems.org/gems/hoe-gemspec2
Vcs:           https://github.com/raggi/hoe-gemspec2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 0
BuildRequires: gem(minitest) >= 5.15
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-seattlerb) >= 1.2
BuildRequires: gem(hoe-git2) >= 1.3
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hoe) >= 0
Provides:      gem(hoe-gemspec2) = 1.3.0


%description
Adds support for generation of gemspec files to Hoe. By default, excludes the
signing key and certificate chain. Use <tt>rake gemspec:full</tt> to include the
signing key and certificate chain.


%if_enabled    doc
%package       -n gem-hoe-gemspec2-doc
Version:       1.3.0
Release:       alt1
Summary:       Adds support for generation of gemspec files to Hoe documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-gemspec2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-gemspec2) = 1.3.0

%description   -n gem-hoe-gemspec2-doc
Adds support for generation of gemspec files to Hoe documentation files.

Adds support for generation of gemspec files to Hoe. By default, excludes the
signing key and certificate chain. Use <tt>rake gemspec:full</tt> to include the
signing key and certificate chain.

%description   -n gem-hoe-gemspec2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-gemspec2.
%endif


%if_enabled    devel
%package       -n gem-hoe-gemspec2-devel
Version:       1.3.0
Release:       alt1
Summary:       Adds support for generation of gemspec files to Hoe development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-gemspec2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-gemspec2) = 1.3.0
Requires:      gem(minitest) >= 5.15
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-seattlerb) >= 1.2
Requires:      gem(hoe-git2) >= 1.3
Requires:      gem(rdoc) >= 4.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7

%description   -n gem-hoe-gemspec2-devel
Adds support for generation of gemspec files to Hoe development package.

Adds support for generation of gemspec files to Hoe. By default, excludes the
signing key and certificate chain. Use <tt>rake gemspec:full</tt> to include the
signing key and certificate chain.

%description   -n gem-hoe-gemspec2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-gemspec2.
%endif


%prep
%setup
%autopatch -p1

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

%if_enabled    doc
%files         -n gem-hoe-gemspec2-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-gemspec2-devel
%doc README.rdoc
%endif


%changelog
* Sat Aug 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.2.0 -> 1.3.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
