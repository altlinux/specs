%define        gemname path_expander

Name:          gem-path-expander
Version:       1.1.0
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/path_expander
Vcs:           https://github.com/seattlerb/path_expander.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Provides:      gem(path_expander) = 1.1.0


%description
PathExpander helps pre-process command-line arguments expanding directories into
their constituent files. It further helps by providing additional mechanisms to
make specifying subsets easier with path subtraction and allowing for
command-line arguments to be saved in a file.

NOTE: this is NOT an options processor. It is a path processor (basically
everything else besides options). It does provide a mechanism for pre-filtering
cmdline options, but not with the intent of actually processing them in
PathExpander. Use OptionParser to deal with options either before or after
passing ARGV through PathExpander.


%package       -n gem-path-expander-doc
Version:       1.1.0
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета path_expander
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(path_expander) = 1.1.0

%description   -n gem-path-expander-doc
PathExpander helps pre-process command-line arguments expanding directories into
their constituent files documentation files.

PathExpander helps pre-process command-line arguments expanding directories into
their constituent files. It further helps by providing additional mechanisms to
make specifying subsets easier with path subtraction and allowing for
command-line arguments to be saved in a file.

NOTE: this is NOT an options processor. It is a path processor (basically
everything else besides options). It does provide a mechanism for pre-filtering
cmdline options, but not with the intent of actually processing them in
PathExpander. Use OptionParser to deal with options either before or after
passing ARGV through PathExpander.

%description   -n gem-path-expander-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета path_expander.


%package       -n gem-path-expander-devel
Version:       1.1.0
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета path_expander
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(path_expander) = 1.1.0
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-path-expander-devel
PathExpander helps pre-process command-line arguments expanding directories into
their constituent files development package.

PathExpander helps pre-process command-line arguments expanding directories into
their constituent files. It further helps by providing additional mechanisms to
make specifying subsets easier with path subtraction and allowing for
command-line arguments to be saved in a file.

NOTE: this is NOT an options processor. It is a path processor (basically
everything else besides options). It does provide a mechanism for pre-filtering
cmdline options, but not with the intent of actually processing them in
PathExpander. Use OptionParser to deal with options either before or after
passing ARGV through PathExpander.

%description   -n gem-path-expander-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета path_expander.


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

%files         -n gem-path-expander-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-path-expander-devel
%doc README.rdoc


%changelog
* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
