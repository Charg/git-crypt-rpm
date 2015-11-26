Name:		git-crypt
Version:	0.5.0
Release:	2%{?dist}
Summary:	Transparent file encryption in git

License:	GPL-3+ with OpenSSL exception
URL:		https://www.agwa.name/projects/git-crypt/
Source0:	https://www.agwa.name/projects/git-crypt/downloads/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	openssl-devel
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl

Requires:	git >= 1.7.2
Requires:	openssl

%description
git-crypt enables transparent encryption and decryption of files in a git repository. Files which you choose to protect are encrypted when committed, and decrypted when checked out. git-crypt lets you freely share a repository containing a mix of public and private content. git-crypt gracefully degrades, so developers without the secret key can still clone and commit to a repository with encrypted files. This lets you store your secret material (such as keys or passwords) in the same repository as your code, without requiring you to lock down your entire repository.

%prep
%setup


%build
make ENABLE_MAN=yes %{?_smp_mflags}


%install
make install ENABLE_MAN=yes PREFIX=%{buildroot}%{_prefix}


%files
%{_bindir}/git-crypt
%{_mandir}/*/*


%doc AUTHORS README.md README THANKS.md NEWS.md NEWS CONTRIBUTING.md RELEASE_NOTES-0.4.1.md COPYING RELEASE_NOTES-0.4.md


%changelog
* Thu Nov 26 2015 Artem Sidorenko <artem.sidorenko@telekom.de> - 0.5.0-2
- Including man pages and docs
* Wed Jun 03 2015 Chris Argeros <chris@argeros.org> - 0.5.0
- Created initial spec
