Name:           twelvemonkeys
Version:        3.13.1
Release:        alt1

Summary:        TwelveMonkeys ImageIO: Additional plug-ins and extensions for Java's ImageIO
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://haraldk.github.io/TwelveMonkeys/
VCS:            https://github.com/haraldk/TwelveMonkeys

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.apache.xmlgraphics:batik-rasterizer-ext)
BuildRequires:  mvn(org.apache.xmlgraphics:batik-extension)
BuildRequires:  mvn(org.apache.xmlgraphics:batik-anim)
BuildRequires:  mvn(org.apache.xmlgraphics:batik-svggen)
BuildRequires:  mvn(org.apache.xmlgraphics:batik-transcoder)
BuildRequires:  mvn(com.github.jai-imageio:jai-imageio-core)

BuildArch:      noarch

%description
TwelveMonkeys ImageIO provides extended image file format support for the Java
platform, through plugins for the javax.imageio.* package.

The main goal of this project is to provide support for file formats not covered
by the JDK. Support for these formats is important, to be able to read data
found "in the wild", as well as to maintain access to data in legacy formats.
As there is lots of legacy data out there, we see the need for open
implementations of readers for popular formats.

%javadoc_package

%package        bom
Summary:        TwelveMonkeys "Bill of Materials" (BOM)
Group:          Development/Java

%description    bom
%summary.

%package        common
Summary:        The TwelveMonkeys Common library. Contains common utility classes
Group:          Development/Java

%description    common
%summary.

%package        contrib
Summary:        Contributions to TwelveMonkeys and code that doesn't fit anywhere else
Group:          Development/Java

%description    contrib
%summary.

%package        imageio-batik
Summary:        ImageIO wrapper for the Batik SVG Toolkit, enabling Scalable Vector Graphics (SVG) support
Group:          Development/Java

%description    imageio-batik
%summary.

%package        imageio-bmp
Summary:        ImageIO plugin for Microsoft Device Independent Bitmap (BMP/DIB) format
Group:          Development/Java

%description    imageio-bmp
%summary.

%package        imageio-clippath
Summary:        Photoshop Clipping Path Support
Group:          Development/Java

%description    imageio-clippath
%summary.

%package        imageio-core
Summary:        TwelveMonkeys ImageIO core support classes
Group:          Development/Java

%description    imageio-core
%summary.

%package        imageio-dds
Summary:        ImageIO plugin for Microsoft Direct DrawSurface (DDS)
Group:          Development/Java

%description    imageio-dds
%summary.

%package        imageio-hdr
Summary:        ImageIO plugin for Radiance RGBE High Dynaimc Range format (HDR)
Group:          Development/Java

%description    imageio-hdr
%summary.

%package        imageio-icns
Summary:        ImageIO plugin for Apple Icon Image (ICNS) format
Group:          Development/Java

%description    imageio-icns
%summary.

%package        imageio-iff
Summary:        ImageIO plugin for Amiga/Electronic Arts Interchange File Format (IFF) type ILBM and PBM format
Group:          Development/Java

%description    imageio-iff
%summary.

%package        imageio-jpeg
Summary:        ImageIO plugin for Joint Photographer Expert Group images (JPEG/JFIF)
Group:          Development/Java

%description    imageio-jpeg
This package also contains:
- Test JPEG plugin and JAI TIFF plugin interoperability.
- Test JPEG plugin and JEP-262 (JDK TIFF plugin) interoperability.

%package        imageio-metadata
Summary:        TwelveMonkeys ImageIO metadata support classes
Group:          Development/Java

%description    imageio-metadata
%summary.

%package        imageio-pcx
Summary:        ImageIO plugin for ZSoft Paintbrush Format (PCX)
Group:          Development/Java

%description    imageio-pcx
%summary.

%package        imageio-pdf
Summary:        ImageIO plugin for Adobe Portable Document Format (PDF)
Group:          Development/Java

%description    imageio-pdf
%summary.

%package        imageio-pict
Summary:        ImageIO plugin for Apple Mac Paint Picture (PICT) format
Group:          Development/Java

%description    imageio-pict
%summary.

%package        imageio-pnm
Summary:        ImageIO plugin for NetPBM Portable Any Map (PNM)
Group:          Development/Java

%description    imageio-pnm
%summary.

%package        imageio-psd
Summary:        ImageIO plugin for Adobe Photoshop Document (PSD)
Group:          Development/Java

%description    imageio-psd
%summary.

%package        imageio-reference
Summary:        Test cases for the JRE provided ImageReader implementations for reference
Group:          Development/Java

%description    imageio-reference
%summary.

%package        imageio-sgi
Summary:        ImageIO plugin for Silicon Graphics Image Format (SGI)
Group:          Development/Java

%description    imageio-sgi
%summary.

%package        imageio-tga
Summary:        ImageIO plugin for Truevision TGA Image Format (TGA)
Group:          Development/Java

%description    imageio-tga
%summary.

%package        imageio-thumbsdb
Summary:        ImageIO plugin for Windows Thumbs DB (Thumbs.db) format
Group:          Development/Java

%description    imageio-thumbsdb
%summary.

%package        imageio-tiff
Summary:        ImageIO plugin for Aldus/Adobe Tagged Image File Format (TIFF)
Group:          Development/Java

%description    imageio-tiff
This package also contains:
- Test TIFF plugin and JDK JPEG plugin interoperability.
- Test TIFF plugin and JAI TIFF plugin Metadata interoperability.

%package        imageio-webp
Summary:        ImageIO plugin for Google WebP File Format (WebP)
Group:          Development/Java

%description    imageio-webp
%summary.

%package        imageio-xwd
Summary:        ImageIO plugin for X11 Window Dump Format (XWD)
Group:          Development/Java

%description    imageio-xwd
%summary.

%package        servlet
Summary:        TwelveMonkeys Servlet support classes
Group:          Development/Java

%description    servlet
%summary.

%package        parent
Summary:        TwelveMonkeys parent POM
Group:          Development/Java

%description    parent
%summary.

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-help-plugin

# for clean tests
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

# missing fonts
rm imageio/imageio-pict/src/test/java/com/twelvemonkeys/imageio/plugins/pict/PICTImageReaderTest.java
rm imageio/imageio-batik/src/test/java/com/twelvemonkeys/imageio/plugins/svg/SVGImageReaderTest.java
rm imageio/imageio-batik/src/test/java/com/twelvemonkeys/imageio/plugins/wmf/WMFImageReaderTest.java

%mvn_package :common-lang common
%mvn_package :common-io common
%mvn_package :common-image common

%mvn_package :imageio-jpeg-jai-interop imageio-jpeg
%mvn_package :imageio-jpeg-jep262-interop imageio-jpeg

%mvn_package :imageio-tiff-jai-interop imageio-tiff
%mvn_package :imageio-tiff-jdk-interop imageio-tiff

%mvn_package :imageio __noinstall

%build
%mvn_build -s

%install
%mvn_install

%files bom -f .mfiles-bom
%doc README.md

%files common -f .mfiles-common
%doc README.md

%files contrib -f .mfiles-contrib
%doc README.md

%files imageio-batik -f .mfiles-imageio-batik
%doc README.md imageio/imageio-batik/license.txt

%files imageio-bmp -f .mfiles-imageio-bmp
%doc README.md imageio/imageio-bmp/license.txt

%files imageio-clippath -f .mfiles-imageio-clippath
%doc README.md imageio/imageio-clippath/license.txt

%files imageio-core -f .mfiles-imageio-core
%doc README.md imageio/imageio-core/license.txt

%files imageio-dds -f .mfiles-imageio-dds
%doc README.md imageio/imageio-dds/license.txt

%files imageio-hdr -f .mfiles-imageio-hdr
%doc README.md imageio/imageio-hdr/license.txt

%files imageio-icns -f .mfiles-imageio-icns
%doc README.md imageio/imageio-icns/license.txt

%files imageio-iff -f .mfiles-imageio-iff
%doc README.md imageio/imageio-iff/license.txt

%files imageio-jpeg -f .mfiles-imageio-jpeg
%doc README.md imageio/imageio-jpeg/license.txt

%files imageio-metadata -f .mfiles-imageio-metadata
%doc README.md imageio/imageio-metadata/license.txt

%files imageio-pcx -f .mfiles-imageio-pcx
%doc README.md imageio/imageio-pcx/license.txt

%files imageio-pdf -f .mfiles-imageio-pdf
%doc README.md imageio/imageio-pdf/license.txt

%files imageio-pict -f .mfiles-imageio-pict
%doc README.md imageio/imageio-pict/license.txt

%files imageio-pnm -f .mfiles-imageio-pnm
%doc README.md imageio/imageio-pnm/license.txt

%files imageio-psd -f .mfiles-imageio-psd
%doc README.md imageio/imageio-psd/license.txt

%files imageio-reference -f .mfiles-imageio-reference
%doc README.md imageio/imageio-reference/license.txt

%files imageio-sgi -f .mfiles-imageio-sgi
%doc README.md imageio/imageio-sgi/license.txt

%files imageio-tga -f .mfiles-imageio-tga
%doc README.md imageio/imageio-tga/license.txt

%files imageio-thumbsdb -f .mfiles-imageio-thumbsdb
%doc README.md imageio/imageio-thumbsdb/license.txt

%files imageio-tiff -f .mfiles-imageio-tiff
%doc README.md imageio/imageio-tiff/license.txt

%files imageio-webp -f .mfiles-imageio-webp
%doc README.md

%files imageio-xwd -f .mfiles-imageio-xwd
%doc README.md

%files servlet -f .mfiles-servlet
%doc README.md servlet/license.txt

%files parent -f .mfiles-twelvemonkeys

%changelog
* Sun Mar 22 2026 Evgeniy Serov <scala@altlinux.org> 3.13.1-alt1
- Initial build for Sisyphus.
