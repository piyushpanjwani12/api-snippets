import com.twilio.sdk.resource.instance.ipmessaging.Role;
import com.twilio.sdk.resource.list.ipmessaging.RoleList;
import com.twilio.sdk.TwilioIPMessagingClient;
import com.twilio.sdk.resource.instance.ipmessaging.Service;

public class TwilioTest {
    // Find your Account Sid and Token at twilio.com/user/account
    public static final String ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    public static final String AUTH_TOKEN = "AUTH_TOKEN";
    public static final String SERVICE_SID = "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";

    public static void main(String args[]) throws TwilioRestException {
        // Initialize the client
        TwilioIPMessagingClient client = new TwilioIPMessagingClient(ACCOUNT_SID, AUTH_TOKEN);
        Service service = client.getService(SERVICE_SID);

        // Get the role
        Role role = service.getRole("ROLE_SID");

        // Delete the role
        boolean didDelete = role.delete();
        System.out.println(didDelete);
    }
}