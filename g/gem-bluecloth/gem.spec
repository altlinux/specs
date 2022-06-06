%define        gemname bluecloth

Name:          gem-bluecloth
Version:       2.2.0
Release:       alt1
Summary:       BlueCloth is a Ruby implementation of John Gruber's Markdown
License:       BSD
Group:         Development/Ruby
Url:           http://deveiate.org/projects/BlueCloth
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(tidy-ext) >= 0.1 gem(tidy-ext) < 1
BuildRequires: gem(rake-compiler) >= 0.7 gem(rake-compiler) < 2
BuildRequires: gem(rspec) >= 2.6 gem(rspec) < 4
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Provides:      gem(bluecloth) = 2.2.0


%description
BlueCloth is a Ruby implementation of John Gruber's
Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML
conversion tool for web writers. To quote from the project page: Markdown allows
you to write using an easy-to-read, easy-to-write plain text format, then
convert it to structurally valid XHTML (or HTML).

It borrows a naming convention and several helpings of interface from
{Redcloth}[http://redcloth.org/], Why the Lucky Stiff's processor for a similar
text-to-HTML conversion syntax called
Textile[http://www.textism.com/tools/textile/].

BlueCloth 2 is a complete rewrite using David Parsons'
Discount[http://www.pell.portland.or.us/~orc/Code/discount/] library, a C
implementation of Markdown. I rewrote it using the extension for speed and
accuracy; the original BlueCloth was a straight port from the Perl version that
I wrote in a few days for my own use just to avoid having to shell out to
Markdown.pl, and it was quite buggy and slow. I apologize to all the good people
that sent me patches for it that were never released.

Note that the new gem is called 'bluecloth' and the old one 'BlueCloth'. If you
have both installed, you can ensure you're loading the new one with the 'gem'
directive:

# Load the 2.0 version gem 'bluecloth', '>= 2.0.0' # Load the 1.0 version gem
'BlueCloth' require 'bluecloth'


%package       -n bluecloth
Version:       2.2.0
Release:       alt1
Summary:       BlueCloth is a Ruby implementation of John Gruber's Markdown executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bluecloth
Group:         Other
BuildArch:     noarch

Requires:      gem(bluecloth) = 2.2.0

%description   -n bluecloth
BlueCloth is a Ruby implementation of John Gruber's Markdown executable(s).

BlueCloth is a Ruby implementation of John Gruber's
Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML
conversion tool for web writers. To quote from the project page: Markdown allows
you to write using an easy-to-read, easy-to-write plain text format, then
convert it to structurally valid XHTML (or HTML).

It borrows a naming convention and several helpings of interface from
{Redcloth}[http://redcloth.org/], Why the Lucky Stiff's processor for a similar
text-to-HTML conversion syntax called
Textile[http://www.textism.com/tools/textile/].

BlueCloth 2 is a complete rewrite using David Parsons'
Discount[http://www.pell.portland.or.us/~orc/Code/discount/] library, a C
implementation of Markdown. I rewrote it using the extension for speed and
accuracy; the original BlueCloth was a straight port from the Perl version that
I wrote in a few days for my own use just to avoid having to shell out to
Markdown.pl, and it was quite buggy and slow. I apologize to all the good people
that sent me patches for it that were never released.

Note that the new gem is called 'bluecloth' and the old one 'BlueCloth'. If you
have both installed, you can ensure you're loading the new one with the 'gem'
directive:

    # Load the 2.0 version gem 'bluecloth', '>= 2.0.0' # Load the 1.0 version gem
    'BlueCloth' require 'bluecloth'

%description   -n bluecloth -l ru_RU.UTF-8
Исполнямка для самоцвета bluecloth.


%package       -n gem-bluecloth-doc
Version:       2.2.0
Release:       alt1
Summary:       BlueCloth is a Ruby implementation of John Gruber's Markdown documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bluecloth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bluecloth) = 2.2.0

%description   -n gem-bluecloth-doc
BlueCloth is a Ruby implementation of John Gruber's Markdown documentation
files.

BlueCloth is a Ruby implementation of John Gruber's
Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML
conversion tool for web writers. To quote from the project page: Markdown allows
you to write using an easy-to-read, easy-to-write plain text format, then
convert it to structurally valid XHTML (or HTML).

It borrows a naming convention and several helpings of interface from
{Redcloth}[http://redcloth.org/], Why the Lucky Stiff's processor for a similar
text-to-HTML conversion syntax called
Textile[http://www.textism.com/tools/textile/].

BlueCloth 2 is a complete rewrite using David Parsons'
Discount[http://www.pell.portland.or.us/~orc/Code/discount/] library, a C
implementation of Markdown. I rewrote it using the extension for speed and
accuracy; the original BlueCloth was a straight port from the Perl version that
I wrote in a few days for my own use just to avoid having to shell out to
Markdown.pl, and it was quite buggy and slow. I apologize to all the good people
that sent me patches for it that were never released.

Note that the new gem is called 'bluecloth' and the old one 'BlueCloth'. If you
have both installed, you can ensure you're loading the new one with the 'gem'
directive:

    # Load the 2.0 version gem 'bluecloth', '>= 2.0.0' # Load the 1.0 version gem
    'BlueCloth' require 'bluecloth'

%description   -n gem-bluecloth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bluecloth.


%package       -n gem-bluecloth-devel
Version:       2.2.0
Release:       alt1
Summary:       BlueCloth is a Ruby implementation of John Gruber's Markdown development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bluecloth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bluecloth) = 2.2.0
Requires:      gem(tidy-ext) >= 0.1 gem(tidy-ext) < 1
Requires:      gem(rake-compiler) >= 0.7 gem(rake-compiler) < 2
Requires:      gem(rspec) >= 2.6 gem(rspec) < 4
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-bluecloth-devel
BlueCloth is a Ruby implementation of John Gruber's Markdown development
package.

BlueCloth is a Ruby implementation of John Gruber's
Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML
conversion tool for web writers. To quote from the project page: Markdown allows
you to write using an easy-to-read, easy-to-write plain text format, then
convert it to structurally valid XHTML (or HTML).

It borrows a naming convention and several helpings of interface from
{Redcloth}[http://redcloth.org/], Why the Lucky Stiff's processor for a similar
text-to-HTML conversion syntax called
Textile[http://www.textism.com/tools/textile/].

BlueCloth 2 is a complete rewrite using David Parsons'
Discount[http://www.pell.portland.or.us/~orc/Code/discount/] library, a C
implementation of Markdown. I rewrote it using the extension for speed and
accuracy; the original BlueCloth was a straight port from the Perl version that
I wrote in a few days for my own use just to avoid having to shell out to
Markdown.pl, and it was quite buggy and slow. I apologize to all the good people
that sent me patches for it that were never released.

Note that the new gem is called 'bluecloth' and the old one 'BlueCloth'. If you
have both installed, you can ensure you're loading the new one with the 'gem'
directive:

    # Load the 2.0 version gem 'bluecloth', '>= 2.0.0' # Load the 1.0 version gem
    'BlueCloth' require 'bluecloth'

%description   -n gem-bluecloth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bluecloth.


%prep
%setup
%autopatch

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
%ruby_gemextdir

%files         -n bluecloth
%doc README.rdoc
%_bindir/bluecloth

%files         -n gem-bluecloth-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-bluecloth-devel
%doc README.rdoc
%ruby_includedir/*


%changelog
* Tue May 17 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- + packaged gem with Ruby Policy 2.0
