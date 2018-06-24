package hello;

public class Greeting {


	private final long id;
	private final String version;
	private final String content;

	public String getVersion() {
		return version;
	}


    public Greeting(long id, String content) {
        this.id = id;
        this.content = content;
        this.version = "2.0";
    }
	public Greeting(long id, String version, String content) {
		super();
		this.id = id;
		this.version = version;
		this.content = content;
	}

    public long getId() {
        return id;
    }

    public String getContent() {
        return content;
    }
    
}
