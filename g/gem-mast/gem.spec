%define        gemname mast

Name:          gem-mast
Version:       1.3.0
Release:       alt1
Summary:       Mast is a command line tool for generating manifests and digests
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://rubyworks.github.com/mast/
Vcs:           git://github.com/rubyworks/mast.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(mast) = 1.3.0


%description
Mast is a command line tool for generating manifests and digests. Mast makes it
easy to compare a manifest to a current directory structure, and to update the
manifest with a simple command by storing the command options it the manifest
file itself.


%package       -n mast
Version:       1.3.0
Release:       alt1
Summary:       Mast is a command line tool for generating manifests and digests executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mast
Group:         Other
BuildArch:     noarch

Requires:      gem(mast) = 1.3.0

%description   -n mast
Mast is a command line tool for generating manifests and digests
executable(s).

Mast is a command line tool for generating manifests and digests. Mast makes it
easy to compare a manifest to a current directory structure, and to update the
manifest with a simple command by storing the command options it the manifest
file itself.

%description   -n mast -l ru_RU.UTF-8
Исполнямка для самоцвета mast.


%package       -n gem-mast-doc
Version:       1.3.0
Release:       alt1
Summary:       Mast is a command line tool for generating manifests and digests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mast
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mast) = 1.3.0

%description   -n gem-mast-doc
Mast is a command line tool for generating manifests and digests documentation
files.

Mast is a command line tool for generating manifests and digests. Mast makes it
easy to compare a manifest to a current directory structure, and to update the
manifest with a simple command by storing the command options it the manifest
file itself.

%description   -n gem-mast-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mast.


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

%files         -n mast
%doc README.rdoc
%_bindir/mast

%files         -n gem-mast-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0
