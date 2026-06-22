%define _unpackaged_files_terminate_build 1

Name: newelle
Version: 1.4.5
Release: alt1

Summary: Ultimate Virtual Assistant
License: GPL-3.0-or-later
Group: Office
URL: https://github.com/qwersyk/Newelle

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/gtk-update-icon-cache
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: pkgconfig(gio-2.0)

Requires: libadwaita-gir
Requires: libgtksourceview5-gir
Requires: libpango-gir
Requires: libvte3-gir
Requires: libwebkitgtk6.0-gir

Requires: python3(cairo)
Requires: python3-module-pygobject3

# see modules/requirements.txt
Requires: python3(requests)
Requires: python3(expandvars)
Requires: python3-module-pillow
Requires: python3(pyaudio)
Requires: python3(pydub)
Requires: python3(openai)
Requires: python3(tiktoken)
Requires: python3(newspaper)
Requires: python3(mcp)
Requires: python3(lxml)
Requires: python3(lxml_html_clean)
Requires: python3(pylatexenc)
Requires: python3(matplotlib)
Requires: python3-module-matplotlib-cairo
Requires: python3-module-matplotlib-gtk4
Requires: python3(markdownify)

Requires: python3(docx2txt)
Requires: python3(gtts)

Requires: python3(numpy)
Requires: python3(six)
Requires: python3(tldextract)

Requires: git
Requires: libportaudio2
Requires: /usr/bin/xdg-open
Requires: python3(pip)
Requires: lsb-release
Requires: /usr/bin/espeak
Requires: /usr/bin/ffplay
Requires: /usr/bin/ffmpeg

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Newelle - Your Ultimate Virtual Assistant.

Features:

* Advanced Customization: Tailor the application with a wide range of
  settings;
* Flexible Model Support: Choose from mutliple AI models and providers to
  fit your specific needs;
* Terminal Command Exection: Execute commands suggested by the AI on the
  fly;
* Extensions: Add your own functionalities and models to Newelle;
* Voice support: Chat hands free with Newelle, supporting many Speech To
  Text and TTS models, with translation options;
* Long Term Memory: Remember conversations from previous chats;
* Chat with documents: Chat with your own documents;
* Web Search: Provide reliable answers using Web Search;
* Website Reading: Scrap informations from websites by appending the
  prefix #https://.. in the prompt;
* Profile Manager: Create settings profiles and switch between them;
* Builtin File Manager: Manage you files with the help of AI;
* Rich Formatting: Supports both Markdown and LaTeX;
* Chat editing: Edit or remove any message and manage your prompts
  easily.

%prep
%setup
%autopatch -p1
sed -i "s|Categories=.*|Categories=Science;ArtificialIntelligence;|" data/io.github.qwersyk.Newelle.desktop.in

%build
%meson
%meson_build

%install
%meson_install

chmod a+x %buildroot%_bindir/newelle

%find_lang %name

%post
echo "WARNING: newelle is a modern application for working with AI LLMs."
echo "         On the first launch it will download a set of Python modules"
echo "         into isolated Python virtual environment at ~/.config/Newelle"
echo "         and later it may/will download local LLMs files and extensions"
echo "         into ~/.cache/Newelle/ and ~/.cache/huggingface depending on"
echo "         user preferences."
echo "         Please note that application can't work without these files."

%check
%meson_test

%files -f %{name}.lang
%doc README.md
%_bindir/newelle
%_datadir/appdata/io.github.qwersyk.Newelle.appdata.xml
%_desktopdir/io.github.qwersyk.Newelle.desktop
%_datadir/glib-2.0/schemas/io.github.qwersyk.Newelle.gschema.xml
%_iconsdir/hicolor/scalable/apps/io.github.qwersyk.Newelle.svg
%_iconsdir/hicolor/symbolic/apps/*.svg
%dir %_datadir/newelle/
%_datadir/newelle/*

%changelog
* Mon Jun 22 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.5-alt1
- New version 1.4.5.

* Sat May 23 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Tue Mar 31 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.7-alt1
- New version 1.3.7.

* Sat Mar 21 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.5-alt1
- New version 1.3.5.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sun Feb 08 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.5-alt1
- New version 1.2.5.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt3
- Added missed espeak, ffplay and ffmpeg run-time dependencies.
- Removed unneeded wget run-time dependency.

* Sun Jan 25 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt2
- Inform user about downloading data into home folder (closes: #57637):
  + Use Python3 pip from the repository.
  + Added post-install warning message about downloading files into home folder.
- Added missed lsb-release dependency.

* Sat Jan 24 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
